---
# Documentation: https://wowchemy.com/docs/managing-content/

title: VMM emulation of Intel hardware transactional memory
subtitle: ''
summary: ''
authors:
- Maciej Swiech
- admin
- Peter A. Dinda
tags: []
categories: []
date: 2014-06-01
lastmod: 2023-03-04T13:21:53-06:00
featured: false
draft: false
venue: ROSS '14

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
publishDate: '2023-03-04T19:21:53.711998Z'
publication_types:
- '1'
abstract: We describe the design, implementation, and evaluation of emulated hardware
  transactional memory, specifically the Intel Haswell Restricted Transactional Memory
  (RTM) architectural extensions for x86/64, within a virtual machine monitor (VMM).
  Our system allows users to investigate RTM on hardware that does not provide it,
  debug their RTM-based transactional software, and stress test it on diverse emulated
  hardware configurations, including potential future configurations that might support
  arbitrary length transactions. Initial performance results suggest that we are able
  to accomplish this approximately 60 times faster than under a full emulator. A noteworthy
  aspect of our system is a novel page-flipping technique that allows us to completely
  avoid instruction emulation, and to limit instruction decoding to only that necessary
  to determine instruction length. This makes it possible to implement RTM emulation,
  and potentially other techniques, far more compactly than would otherwise be possible.
  We have implemented our system in the context of the Palacios VMM. Our techniques
  are not specific to Palacios, and could be implemented in other VMMs.
publication: '*Proceedings of the 4th International Workshop on Runtime and Operating
  Systems for Supercomputers*'
links:
- name: DOI
  icon_pack: ai
  icon: doi
  url: https://doi.org/10.1145/2612262.2612265
- name: ACM
  icon_pack: ai
  icon: acmdl
  url: https://dl.acm.org/doi/10.1145/2612262.2612265
- name: PDF
  icon_pack: fas
  icon: file-pdf
  url: http://pdinda.org/Papers/ross14.pdf
---
