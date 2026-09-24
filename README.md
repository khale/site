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

## Preview locally (Docker)

```sh
docker compose up --build        # first time; afterwards just `docker compose up`
open http://localhost:8000       # rebuilds on save; refresh the browser to see changes
docker compose down
```

Other one-offs:

```sh
docker compose run --rm site build                   # production build into ./public
docker compose run --rm site news "Paper accepted"   # add a news item dated today
```

Without Docker, the same commands work with plain Python:
`pip install -r requirements.txt`, then `python3 build.py serve`.

## Skins

Set `skin:` in `site.yaml`. Each skin is one CSS file in `static/css/skins/` that overrides
the color/font tokens and a few rules in `static/css/site.css`:

- `paper`: Charter headings, warm white, blue links (no web fonts)
- `terminal`: IBM Plex Sans/Mono, flat, green accent
- `sidebar`: Inter, white, fixed left navigation on wide screens
- `classic`: Source Serif, centered masthead, oxblood accent

In the local preview there's a **skin** picker in the bottom-right corner (preview only; it
isn't in the deployed site), or run `SKIN=classic docker compose up`. To make a new
skin, copy one of the files and change the tokens.

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
static/             copied as-is (css/, css/skins/, fonts/, img/, papers/, cv.pdf, ...)
Dockerfile, compose.yaml   local preview
```

The lab page (`templates/lab.html`, `static/css/lab.css`, `data/lab.yaml`, `pages/lab.md`)
is self-contained, so it can be moved into its own repo later. It only uses
the shared header and footer, plus a link to the publication list.
