---
# Documentation: https://wowchemy.com/docs/managing-content/

title: A Case for Transforming Parallel Runtimes Into Operating System Kernels
subtitle: ''
summary: ''
authors:
- admin
- Peter A. Dinda
tags:
- hrts
- hybrid runtimes
- nautilus
- parallel runtimes
categories: []
date: '2015-06-01'
lastmod: 2023-03-04T13:34:36-06:00
featured: false
draft: false
venue: HPDC '15
award: Best Short Paper Presentation

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-03-04T19:34:36.579801Z'
publication_types:
- '1'
abstract: The needs of parallel runtime systems and the increasingly sophisticated
  languages and compilers they support do not line up with the services provided by
  general-purpose OSes. Furthermore, the semantics available to the runtime are lost
  at the system-call boundary in such OSes. Finally, because a runtime executes at
  user-level in such an environment, it cannot leverage hardware features that require
  kernel-mode privileges---a large portion of the functionality of the machine is
  lost to it. These limitations warp the design, implementation, functionality, and
  performance of parallel runtimes. We summarize the case for eliminating these compromises
  by transforming parallel runtimes into OS kernels. We also demonstrate that it is
  feasible to do so. Our evidence comes from Nautilus, a prototype kernel framework
  that we built to support such transformations. After describing Nautilus, we report
  on our experiences using it to transform three very different runtimes into kernels.
publication: '*Proceedings of the 24th ACM Symposium on High-performance Parallel
  and Distributed Computing (HPDC 2015)*'
links:
- name: DOI
  icon_pack: ai
  icon: doi
  url: https://doi.org/10.1145/2749246.2749264
- name: ACM
  icon_pack: ai
  icon: acmdl
  url: https://dl.acm.org/doi/10.1145/2749246.2749264
- name: PDF
  icon_pack: fas
  icon: file-pdf
  url: http://pdinda.org/Papers/hpdc15.pdf
---
