---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Collaborative Research: PPoSS: Planning: Unifying Software and Hardware to Achieve Performant and Scalable Zero-cost Parallelism in the Heterogeneous Future"
summary: ""
authors: [admin, Peter Dinda, Simone Campanoni, Nikos Hardavellas, Umut Acar]
tags: [os, systems, arch, compilers, pl]
categories: []
date: 2020-08-19

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
# projects: [interweaving]
---

NSF Award [CCF-2028958](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2028958&HistoricalAwards=false);
$41,627 (Collaborative total: $250K); October 2020 through September 2021. This project is a collaborative effort with
[Peter Dinda](http://pdinda.org), [Simone Campanoni](https://users.cs.northwestern.edu/~simonec/), and [Nikos Hardavellas](https://users.cs.northwestern.edu/~hardav/)
at [Northwestern University](https://northwestern.edu), and [Umut acar](http://www.umut-acar.org/) at [Carnegie Mellon University](https://www.cmu.edu/).

Exploiting parallelism is essential to making full use of computer systems, and
thus is intrinsic to most applications. Building parallel programs that can
truly achieve the performance the hardware is capable of is extremely
challenging even for experts. It requires a firm grasp of concepts that range
from the very highest level to the very lowest, and that range is rapidly
expanding. This project approaches this challenge along two lines, "theory
down" and "architecture up". The first strives to simplify parallel programming
through languages and algorithms. The second line strives to accelerate
parallel programs through compilers, operating systems, and the hardware. The
project's novelty is to bridge these two lines, which are usually treated quite
distinctly by the research community. The unified team of researchers is
addressing a specific subproblem, scheduling, and then determining how to
expand out from it. The project's impact is in making it possible for ordinary
programmers to program future parallel systems in a very high-level way, yet
achieve the performance possible on the machine.

The project studies an "intermediate representation out" approach to making
high-level parallel abstractions implementable so that they can be used with
zero cost. A core idea is to expand the compiler's intermediate representation
such that it can capture both high-level parallel concepts and low-level
machine and operating system structures, thus allowing full stack optimization.
This planning project will flesh out this concept and set the stage for
a larger scale effort in the future.


