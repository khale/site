---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Collaborative Research: PPoSS: Planning: Towards an Integrated, Full-stack System for Memory-centric Computing"
summary: ""
authors: [Rujia Wang, admin, Xian-He Sun, Peng Jiang]
tags: [systems, arch, os, pl]
categories: []
date: 2020-08-23

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

NSF Award CCF-2029014;
$185,473 (Collaborative total: $250K); January 2021 through December 2021. This project is a collaborative effort with
[Rujia Wang](https://rujiawang.github.io/) and [Xian-He Sun](http://www.cs.iit.edu/~scs/sun/) at IIT and [Peng Jiang](https://homepage.divms.uiowa.edu/~penjiang/) at the [University of Iowa](https://uiowa.edu/).


As the volume of data being processed by today's systems continues to grow, the
traditional organization of memory systems is shifting to accommodate that
accelerating growth. Data-centric applications are becoming common, from
scientific simulation to emerging distributed machine learning, and irregular
graph mining algorithms. Such applications not only require a large amount of
data to compute and store, but they also generate massive amounts of
intermediate data to move around the compute resources.  Therefore, the memory
system has become the bottleneck of high performance computing.  Memory-centric
computing is a potential solution to overcome the limitations of current
systems. To mitigate bandwidth limitations, compute logic can be added near or
in memory chips, so that we need not move data all the way up to the processing
units. To overcome memory capacity limitations, a remote memory pool can be
added to the system so that all compute units can access it via a fast
interconnect.  Both solutions are promising for breaking down the memory wall.
However, simply combining the two solutions will not realize their full
potential. We need to properly integrate the architecture and revisit the full
system stack through collaborative designs to make it more usable for
applications and enable more efficient computing.

In this work, we propose an integrated, full-stack System to enable
Memory-Centric Computing (SMC2).  We target a system that has near-memory data
processors (NDP) as well as an extendable memory pool.  We work on the entire
system stack to minimize the performance impact of memory accesses from the
research tasks in architecture, SW/HW interface, programming model/compiler,
and performance model/optimization. First, we propose to utilize the NDP
hardware to build an active memory system that supports intelligent data
prefetch and speculative data push, which can overlap the data access time with
computation. Next, we revisit current memory management mechanisms in order to
support NDP function calls, data push operations and virtualization. The new
SW/HW interface allows us to propose a new programming model, which can allow
the programmer to specify which tasks can run on the NDP resources, and allow
efficient NDP to NDP communication. Lastly, we try to optimize the system
performance with the help of NDP through a new memory-centric performance model
and a global performance optimization framework. Putting the four pieces
together, our proposed system support can maximize the performance of
memory-centric computing with new system abstractions and theories.

