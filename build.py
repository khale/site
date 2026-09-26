#!/usr/bin/env python3
"""
Static site builder for halek.co.

    python3 build.py              build the site into ./public
    python3 build.py serve        build, serve on http://localhost:8000, rebuild on change
                                  (HOST / PORT env vars override; SKIN=name previews a skin)
    python3 build.py news "text"  add a news item dated today to data/news.yaml

Inputs (all plain text, no front-matter boilerplate):
    site.yaml            name, nav, profile links
    pubs.bib             the one publication list (see README for the extra fields)
    data/news.yaml       news items: date + markdown text
    data/teaching.yaml   courses grouped by institution
    data/lab.yaml        HExSA lab people
    pages/*.md           free-form pages (bio, personal, recruiting, ...)
    templates/*.html     Jinja2 templates
    static/              copied verbatim into public/
"""
import datetime as dt
import html
import http.server
import os
import re
import shutil
import sys
import threading
import time
from pathlib import Path

import jinja2
import markdown as md_lib
import yaml

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "public"

# ---------------------------------------------------------------- BibTeX ----

MONTHS = {m: i for i, m in enumerate(
    "jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}
MONTH_NAMES = ["", "January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

# Fields that exist only for this website; stripped from the per-paper cite.bib.
SITE_FIELDS = {"venue", "award", "ugrad", "badges", "code", "artifact", "slides",
               "video", "website", "hidden", "pdf", "arxiv"}

ACM_BADGES = {
    "available": "Artifacts Available",
    "functional": "Artifacts Evaluated – Functional",
    "reusable": "Artifacts Evaluated – Reusable",
    "reproduced": "Results Reproduced",
    "replicated": "Results Replicated",
}


def _read_braced(s, i):
    """s[i] == '{' or '"'; return (value, index after closing delimiter)."""
    close = "}" if s[i] == "{" else '"'
    depth, j = 0, i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        if close == '"' and c == '"' and j != i and depth == 0:
            return s[i + 1:j], j + 1
        if close == "}" and depth == 0:
            return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unterminated value near: " + s[i:i + 60])


def parse_bib(text):
    """Minimal BibTeX parser -> list of dicts with 'type', 'key', and lowercase fields."""
    entries, i = [], 0
    while True:
        at = text.find("@", i)
        if at < 0:
            break
        m = re.match(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text[at:])
        if not m:
            i = at + 1
            continue
        etype, key = m.group(1).lower(), m.group(2)
        if etype in ("comment", "string", "preamble"):
            i = at + 1
            continue
        e = {"type": etype, "key": key}
        j = at + m.end()
        while j < len(text):
            fm = re.match(r"\s*(\w+)\s*=\s*", text[j:])
            if not fm:
                end = re.match(r"\s*,?\s*\}", text[j:])
                j += end.end() if end else 1
                break
            name = fm.group(1).lower()
            j += fm.end()
            if text[j] in '{"':
                val, j = _read_braced(text, j)
            else:
                vm = re.match(r"[^,}\s]+", text[j:])
                val = vm.group(0)
                j += vm.end()
            e[name] = " ".join(val.split())
            cm = re.match(r"\s*,", text[j:])
            if cm:
                j += cm.end()
        entries.append(e)
        i = j
    return entries


def delatex(s):
    s = s.replace("\\&", "&").replace("---", "—").replace("--", "–")
    s = s.replace("\\%", "%").replace("~", " ")
    s = re.sub(r"\\[a-zA-Z]+\s*\{([^{}]*)\}", r"\1", s)   # \emph{x} -> x
    return s.replace("{", "").replace("}", "")


def format_name(n):
    n = n.strip()
    if "," in n:
        last, first = [p.strip() for p in n.split(",", 1)]
        n = f"{first} {last}"
    return delatex(n)


def bib_to_pub(e, me):
    authors = [format_name(a) for a in re.split(r"\s+and\s+", e.get("author", "")) if a.strip()]
    month = e.get("month", "").strip().lower()
    mnum = MONTHS.get(month[:3], 0) if not month.isdigit() else int(month)
    year = int(e.get("year", "0"))
    where = e.get("booktitle") or e.get("journal") or e.get("institution") or ""
    if e["type"] == "techreport" and e.get("number"):
        where = f"{where}, Technical Report {e['number']}" if where else f"Technical Report {e['number']}"
    if e["type"] == "article" and e.get("volume"):
        where += f" {e['volume']}" + (f"({e['number']})" if e.get("number") else "")
    if e["type"] == "misc" and e.get("archiveprefix", "").lower() == "arxiv":
        where = f"arXiv:{e.get('eprint', '')}"

    links = []
    def add(label, url):
        if url:
            links.append({"label": label, "url": url})
    add("PDF", e.get("pdf"))
    if e.get("doi"):
        add("DOI", "https://doi.org/" + e["doi"])
    elif e.get("url"):
        add("Publisher", e["url"])
    arxiv = e.get("arxiv") or (e.get("eprint") if e.get("archiveprefix", "").lower() == "arxiv" else "")
    if arxiv:
        add("arXiv", arxiv if arxiv.startswith("http") else "https://arxiv.org/abs/" + arxiv)
    add("Code", e.get("code"))
    add("Artifact", e.get("artifact"))
    add("Slides", e.get("slides"))
    add("Video", e.get("video"))
    add("Website", e.get("website"))

    badges = [b.strip().lower() for b in e.get("badges", "").split(",") if b.strip()]
    # HALE:2015:NAUTILUS -> hale-2015-nautilus; hale2021coalescent -> hale-2021-coalescent
    slug = e["key"].lower().replace(":", "-")
    slug = re.sub(r"^([a-z]+)(\d{4})([a-z].*)$", r"\1-\2-\3", slug)
    return {
        "key": e["key"],
        "slug": slug,
        "title": delatex(e.get("title", "")),
        "authors": [{"name": a, "me": any(a.endswith(x) for x in me)} for a in authors],
        "venue": e.get("venue") or e.get("series") or "",
        "where": delatex(where),
        "year": year,
        "month": mnum,
        "date_str": (MONTH_NAMES[mnum] + " " if mnum else "") + str(year),
        "abstract": delatex(e.get("abstract", "")),
        "award": e.get("award", ""),
        "ugrad": e.get("ugrad", "").lower() in ("true", "yes", "1"),
        "badges": [{"id": b, "label": ACM_BADGES.get(b, b)} for b in badges],
        "links": links,
        "hidden": e.get("hidden", "").lower() in ("true", "yes", "1"),
        "bibtex": to_bibtex(e, drop=SITE_FIELDS | {"abstract"}),
        "meta": scholar_meta(e, authors, year, mnum),
    }


def scholar_meta(e, authors, year, month):
    """(name, content) pairs for Google Scholar's citation_* meta tags."""
    m = [("citation_title", delatex(e.get("title", "")))]
    m += [("citation_author", a) for a in authors]
    m.append(("citation_publication_date", f"{year}/{month:02d}" if month else str(year)))
    if e["type"] == "article":
        m += [("citation_journal_title", delatex(e.get("journal", ""))),
              ("citation_volume", e.get("volume", "")), ("citation_issue", e.get("number", ""))]
    elif e["type"] == "techreport":
        m += [("citation_technical_report_institution", delatex(e.get("institution", ""))),
              ("citation_technical_report_number", e.get("number", ""))]
    elif e.get("booktitle"):
        m.append(("citation_conference_title", delatex(e["booktitle"])))
    pages = re.split(r"\s*[-–—]+\s*", e.get("pages", ""))
    if len(pages) == 2:
        m += [("citation_firstpage", pages[0]), ("citation_lastpage", pages[1])]
    m += [("citation_publisher", delatex(e.get("publisher", ""))), ("citation_doi", e.get("doi", "")),
          ("citation_isbn", e.get("isbn", ""))]
    return [(k, v) for k, v in m if v]


def to_bibtex(e, drop=()):
    fields = [(k, v) for k, v in e.items() if k not in ("type", "key") and k not in drop]
    w = max((len(k) for k, _ in fields), default=0)
    body = ",\n".join(f"  {k.ljust(w)} = {{{v}}}" for k, v in fields)
    return f"@{e['type']}{{{e['key']},\n{body}\n}}\n"


def load_pubs(me):
    entries = parse_bib((ROOT / "pubs.bib").read_text(encoding="utf-8"))
    seen, pubs = set(), []
    for e in entries:
        if e["key"] in seen:
            print(f"warning: duplicate bib key {e['key']} (keeping first)", file=sys.stderr)
            continue
        seen.add(e["key"])
        p = bib_to_pub(e, me)
        if not p["hidden"]:
            pubs.append(p)
    pubs.sort(key=lambda p: (p["year"], p["month"]), reverse=True)
    return pubs

# ------------------------------------------------------------ content ------

def md(text):
    h = md_lib.markdown(text or "", extensions=["extra", "smarty", "toc"], output_format="html5")
    return re.sub(r"&lsquo;(\d\d)\b", r"&rsquo;\1", h)   # IPDPS '26 -> ’26, not ‘26


def md_inline(text):
    h = md(text).strip()
    return re.sub(r"^<p>(.*)</p>$", r"\1", h, flags=re.S)


def read_page(path):
    raw = path.read_text(encoding="utf-8")
    meta, body = {}, raw
    if raw.startswith("---"):
        _, fm, body = raw.split("---", 2)
        meta = yaml.safe_load(fm) or {}
    meta["content"] = md(body)
    meta["slug"] = path.stem
    return meta


def load_yaml(name):
    p = ROOT / "data" / name
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else None


def as_date(d):
    if isinstance(d, dt.datetime):
        return d.date()
    if isinstance(d, dt.date):
        return d
    s = str(d)
    for fmt in ("%Y-%m-%d", "%Y-%m"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    raise ValueError(f"bad date in news.yaml: {d!r} (use YYYY-MM-DD or YYYY-MM)")

# -------------------------------------------------------------- build ------

DEV = False   # set by `serve`: adds the skin switcher


def build():
    t0 = time.time()
    site = yaml.safe_load((ROOT / "site.yaml").read_text(encoding="utf-8"))
    site["skin"] = os.environ.get("SKIN") or site.get("skin", "paper")
    site["same_as"] = [l["url"] for l in site.get("links", []) if l["url"].startswith("http")]
    skins = sorted(p.stem for p in (ROOT / "static/css/skins").glob("*.css"))
    if site["skin"] not in skins:
        sys.exit(f"unknown skin {site['skin']!r}; available: {', '.join(skins)}")
    pubs = load_pubs(site.get("highlight_names", []))

    news = []
    for n in load_yaml("news.yaml") or []:
        d = as_date(n["date"])
        news.append({"date": d, "date_str": d.strftime("%b %Y"), "html": md_inline(n["text"])})
    news.sort(key=lambda n: n["date"], reverse=True)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ROOT / "templates"),
                             autoescape=jinja2.select_autoescape(["html"]),
                             trim_blocks=True, lstrip_blocks=True)
    env.globals.update(site=site, now=dt.date.today(), dev=DEV, skins=skins)

    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT)

    urls = []

    def render(url, template, **ctx):
        urls.append(url)
        dest = OUT / url.strip("/") / "index.html" if url != "/" else OUT / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(env.get_template(template).render(url=url, **ctx), encoding="utf-8")

    pages = {p.stem: read_page(p) for p in sorted((ROOT / "pages").glob("*.md"))}

    render("/", "home.html", page=pages["index"], news=news[:site.get("home_news", 5)],
           pubs=pubs[:site.get("home_pubs", 8)])
    render("/publication/", "pubs.html", title="Publications", pubs=pubs)
    for p in pubs:
        render(f"/publication/{p['slug']}/", "pub.html", title=p["title"], pub=p)
        (OUT / "publication" / p["slug"] / "cite.bib").write_text(p["bibtex"], encoding="utf-8")
    render("/news/", "news.html", title="News", news=news)
    render("/teaching/", "teaching.html", title="Teaching", teaching=load_yaml("teaching.yaml"))
    render("/lab/", "lab.html", title="HExSA Lab", lab=load_yaml("lab.yaml"),
           page=pages.get("lab"))
    for slug, page in pages.items():
        if slug in ("index", "lab"):
            continue
        render(f"/{slug}/", page.get("template", "page.html"), title=page.get("title", slug),
               page=page)
    (OUT / "404.html").write_text(env.get_template("page.html").render(
        url="/404.html", title="Not found",
        page={"title": "Page not found", "content": '<p>Try the <a href="/">home page</a>.</p>'}),
        encoding="utf-8")

    base = site["url"].rstrip("/")
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{html.escape(base + u)}</loc></url>\n" for u in sorted(urls))
        + "</urlset>\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n",
                                    encoding="utf-8")

    print(f"built {len(pubs)} pubs, {len(news)} news items, {len(pages)} pages, skin '{site['skin']}' "
          f"in {time.time() - t0:.2f}s -> {OUT.relative_to(ROOT)}/")

# -------------------------------------------------------------- serve ------

def snapshot():
    watch = [ROOT / "site.yaml", ROOT / "pubs.bib", ROOT / "build.py"]
    for d in ("data", "pages", "templates", "static"):
        watch += [p for p in (ROOT / d).rglob("*") if p.is_file()]
    return {p: p.stat().st_mtime for p in watch if p.exists()}


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(OUT), **k)

    def log_message(self, *a):
        pass


def serve(port=8000):
    global DEV
    DEV = True
    build()
    host = os.environ.get("HOST", "127.0.0.1")
    httpd = http.server.ThreadingHTTPServer((host, port), QuietHandler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    print(f"serving http://localhost:{port}/  (Ctrl-C to stop; rebuilds on save, refresh to see)")
    last = snapshot()
    try:
        while True:
            time.sleep(1)
            cur = snapshot()
            if cur != last:
                last = cur
                try:
                    build()
                except Exception as ex:  # keep serving on template/data errors
                    print("build failed:", ex, file=sys.stderr)
    except KeyboardInterrupt:
        httpd.shutdown()


def add_news(text):
    path = ROOT / "data" / "news.yaml"
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    head, sep, rest = old.partition("\n- ")
    dumped = yaml.safe_dump(text, width=10**6).strip()
    if dumped.endswith("..."):          # yaml's end-of-document marker for plain scalars
        dumped = dumped[:-3].strip()
    item = f"- date: {dt.date.today().isoformat()}\n  text: {dumped}\n"
    if sep:   # keep the header comment, insert new item first
        path.write_text(f"{head}\n{item}\n- {rest}", encoding="utf-8")
    else:
        path.write_text(old.rstrip() + "\n\n" + item, encoding="utf-8")
    print("added to data/news.yaml:\n" + item)


if __name__ == "__main__":
    sys.stdout.reconfigure(line_buffering=True)
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "build":
        build()
    elif cmd == "serve":
        serve(int(sys.argv[2]) if len(sys.argv) > 2 else int(os.environ.get("PORT", 8000)))
    elif cmd == "news" and len(sys.argv) > 2:
        add_news(" ".join(sys.argv[2:]))
    else:
        print(__doc__)
        sys.exit(1)
