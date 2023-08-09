---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Collaborative Research: CSR: Medium: Towards A Unified Memory-centric Computing System with Cross-layer Support"
summary: ""
authors: [Rujia Wang, Xian-He Sun, admin, Peng Jiang]
tags: [systems, arch, os, pl]
categories: []
date: 2023-08-09

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
projects: [next-gen-ndp]
---

NSF Award CNS-2310422;
$886,226 ($1M collaborative total); October 2023 through September 2026. This project is a collaborative effort with
[Rujia Wang](https://rujiawang.github.io/) and [Xian-He Sun](http://www.cs.iit.edu/~scs/sun/) at IIT and [Peng Jiang](https://homepage.divms.uiowa.edu/~penjiang/) at the [University of Iowa](https://uiowa.edu/).

Data-centric applications, from scientific simulation to emerging machine
learning and data mining algorithms, are becoming prevalent. These applications
not only require a large amount of data to compute and store, but also generate
massive amounts of intermediate data being moved around the compute resources.
Therefore, memory systems have become the bottleneck of computing.
Memory-centric computing is a potential solution to overcome the unprecedented
memory performance bottleneck. To mitigate bandwidth limitations, computation
logic can be added near or in memory chips to reduce data access delay and data
movement cost. To overcome memory capacity limitations, the system can
incorporate a shared memory pool that all compute units can directly access.
Both these memory-centric solutions are promising and machine feasible.
However, simply using or combining the two solutions will not realize their
full potential. We need to properly integrate the architecture and revisit the
full system stack through collaborative designs to make these new technologies
more effective for applications and enable more efficient computing. In this
proposal, we propose an integrated, full-stack, cross-layer system to enable
Unified Memorycentric Computing (UniMCC). We target systems that have
near-memory data processors (NDPs) as well as a disaggregated shared memory
pool. We work on the entire system stack to utilize these newly proposed
hardware solutions from a unified viewpoint of architecture, SW/HW interface,
code generation and runtime support, and performance modeling and optimization.
We first build an active memory system that supports intelligent data push
operations to utilize the NDP hardware. We then revisit existing system
software to support features like NDP function calls, data push operations. We
also provide a new memory-centric programming model with compiler and runtime
optimization for efficient code generation. Lastly, we propose a global
performance optimization framework to coordinate all our efforts for the best
overall system performance. Putting the four pieces together, our proposed
UniMCC system will maximize the potential of NDPs and disaggregated memories
and lift memory-centric computing to a new level.
