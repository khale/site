---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Multiverse: Easy Conversion of Runtime Systems into OS Kernels via Automatic
  Hybridization'
subtitle: ''
summary: ''
authors:
- admin
- Conor Hetland
- Peter Dinda
tags: []
categories: []
date: '2017-07-01'
lastmod: 2023-03-03T14:54:06-06:00
featured: false
draft: false
venue: ICAC '17

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
publishDate: '2023-03-03T20:54:06.624451Z'
publication_types:
- '1'
abstract: The hybrid runtime (HRT) model offers a path towards high performance and
  efficiency. By integrating the OS kernel, runtime, and application, an HRT allows
  the runtime developer to leverage the full feature set of the hardware and specialize
  OS services to the runtime's needs. However, conforming to the HRT model currently
  requires a port of the runtime to the kernel level, for example to the Nautilus
  kernel framework, and this requires knowledge of kernel internals. In response,
  we developed Multiverse, a system that bridges the gap between a built-from-scratch
  HRT and a legacy runtime system. Multiverse allows unmodified applications and runtimes
  to be brought into the HRT model without any porting effort whatsoever by splitting
  the execution of the application between the domains of a legacy OS and an HRT environment.
  We describe the design and implementation of Multiverse and illustrate its capabilities
  using the massive, widely-used Racket runtime system.
publication: '*Proceedings of the IEEE International Conference on Autonomic Computing*'
links:
- name: DOI
  icon_pack: ai
  icon: doi
  url: https://dx.doi.org/10.1109/ICAC.2017.24
- name: IEEE
  icon_pack: ai
  icon: ieee
  url: https://ieeexplore.ieee.org/abstract/document/8005347
- name: arXiv
  icon_pack: ai
  icon: arxiv
  url: https://arxiv.org/abs/1901.06360
- name: PDF
  icon_pack: fas
  icon: file-pdf
  url: https://users.cs.northwestern.edu/~pdinda/Papers/icac17.pdf

---
