# halek.co

Personal site for Kyle C. Hale, plus the HExSA lab page. One Python script (`build.py`, ~350 lines)
turns a few plain-text files into static HTML. There's no theme, framework or Hugo.

## Everyday edits

| To…                      | Edit                   | How                                                                 |
|--------------------------|------------------------|---------------------------------------------------------------------|
| Add a paper              | `pubs.bib`             | Paste the BibTeX entry and add `venue = {ASPLOS '27}` (plus any extras below) |
| Add a news item          | `data/news.yaml`       | Add `- date: 2026-10-01` / `text: …`, or run `python3 build.py news "…"` |
| Add a course or term     | `data/teaching.yaml`   | Add one line under the course                                       |
| Update lab members       | `data/lab.yaml`        | Move a line from `current` to `alumni`                              |
| Change bio / pages       | `pages/*.md`           | Markdown. `index.md` is the home-page bio                           |
| Change nav, links, counts | `site.yaml`           |                                                                     |
| Replace CV               | `static/cv.pdf`        |                                                                     |

### Extra BibTeX fields the site understands

BibTeX and LaTeX ignore these, so the same `.bib` still works in papers.

```bibtex
  venue    = {EuroSys '22},                 % pill label (defaults to `series`)
  award    = {Best Paper Award},            % gold pill
  ugrad    = {true},                        % "Undergraduate Research" pill
  badges   = {available, functional, reproduced},   % ACM artifact badges
  pdf      = {/papers/foo.pdf},             % put the file in static/papers/
  arxiv    = {2104.11324},
  code     = {https://github.com/...},
  artifact = {https://zenodo.org/...},
  slides   = {...},  video = {...},  website = {...},
  hidden   = {true},                        % keep in .bib, leave off the site
```

The DOI button comes from `doi`. Each paper gets `/publication/<key>/` (the key is lowercased
and `:` becomes `-`), with the abstract and a clean `cite.bib` that has these extra fields removed.

## Preview locally

```sh
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt   # once
python3 build.py serve          # http://localhost:8000. Rebuilds on save; refresh the page to see changes
python3 build.py                # one-off build into ./public
```

## Deploy

Netlify runs `python3 build.py` (see `netlify.toml`) and publishes `public/`.
`static/_redirects` keeps old Hugo-era URLs working.

## Layout

```
build.py            the whole generator (~350 lines)
site.yaml           name, nav, profile links
pubs.bib            publications
data/               news.yaml, teaching.yaml, lab.yaml
pages/              markdown pages -> /<name>/
templates/          Jinja2 HTML templates
static/             copied as-is (css/, img/, papers/, cv.pdf, ...)
```

The lab page (`templates/lab.html`, `static/css/lab.css`, `data/lab.yaml`, `pages/lab.md`)
is self-contained, so it can be moved into its own repo later. It only uses
the shared header and footer, plus a link to the publication list.
