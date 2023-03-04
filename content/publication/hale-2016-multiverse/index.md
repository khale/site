---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Automatic Hybridization of Runtime Systems
subtitle: ''
summary: ''
authors:
- admin
- Conor Hetland
- Peter A. Dinda
tags:
- hybrid runtimes
- automatic hybridization
- runtime systems
- operating systems
- multiverse
categories: []
date: '2016-05-01'
lastmod: 2023-03-03T14:54:06-06:00
featured: false
draft: false
venue: HPDC '16

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
publishDate: '2023-03-03T20:54:06.335049Z'
publication_types:
- '1'
abstract: The hybrid runtime (HRT) model offers a plausible path towards high performance
  and efficiency. By integrating the OS kernel, parallel runtime, and application,
  an HRT allows the runtime developer to leverage the full privileged feature set
  of the hardware and specialize OS services to the runtime's needs. However, conforming
  to the HRT model currently requires a complete port of the runtime and application
  to the kernel level, for example to our Nautilus kernel framework, and this requires
  knowledge of kernel internals. In response, we developed Multiverse, a system that
  bridges the gap between a built-from-scratch HRT and a legacy runtime system. Multiverse
  allows existing, unmodified applications and runtimes to be brought into the HRT
  model without any porting effort whatsoever. Developers simply recompile their package
  with our compiler toolchain, and Multiverse automatically splits the execution of
  the application between the domains of a legacy OS and an HRT environment. To the
  user, the package appears to run as usual on Linux, but the bulk of it now runs
  as a kernel. The developer can then incrementally extend the runtime and application
  to take advantage of the HRT model. We describe the design and implementation of
  Multiverse, and illustrate its capabilities using the Racket runtime system.
publication: '*Proceedings of the 25th ACM International Symposium on High-Performance
  Parallel and Distributed Computing*'
links:
- name: DOI
  icon_pack: ai
  icon: doi
  url: https://doi.org/10.1145/2907294.2907309
- name: ACM
  icon_pack: ai
  icon: acmdl
  url: https://dl.acm.org/doi/10.1145/2907294.2907309
---
