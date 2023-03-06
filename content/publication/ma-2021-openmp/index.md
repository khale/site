---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Paths to OpenMP in the Kernel
subtitle: ''
summary: ''
authors:
- Jiacheng Ma
- Wenyi Wang
- Aaron Nelson
- Michael Cuevas
- Brian Homerding
- Conghao Liu
- Zhen Huang
- Simone Campanoni
- admin
- Peter Dinda
tags:
- OpenMP
- parallelism
- operating systems
categories: []
date: '2021-01-01'
lastmod: 2023-03-04T12:55:25-06:00
featured: false
draft: false
venue: SC '21
ugrad: true

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
publishDate: '2023-03-04T18:55:24.956053Z'
publication_types:
- '1'
abstract: OpenMP implementations make increasing demands on the kernel. We take the
  next step and consider bringing OpenMP into the kernel. Our vision is that the entire
  OpenMP application, run-time system, and a kernel framework is interwoven to become
  the kernel, allowing the OpenMP implementation to take full advantage of the hardware
  in a custom manner. We compare and contrast three approaches to achieving this goal.
  The first, runtime in kernel (RTK), ports the OpenMP runtime to the kernel, allowing
  any kernel code to use OpenMP pragmas. The second, process in kernel (PIK) adds
  a specialized process abstraction for running user-level OpenMP code within the
  kernel. The third, custom compilation for kernel (CCK), compiles OpenMP into a form
  that leverages the kernel framework without any intermediaries. We describe the
  design and implementation of these approaches, and evaluate them using NAS and other
  benchmarks.
publication: '*Proceedings of the International Conference for High Performance Computing,
  Networking, Storage and Analysis*'
links:
- name: DOI
  icon_pack: ai
  icon: doi
  url: https://doi.org/10.1145/3458817.3476183
- name: DOI
  icon_pack: ai
  icon: acm
  url: https://dl.acm.org/doi/10.1145/3458817.3476183
- name: PDF
  icon_pack: fas
  icon: file-pdf
  url: https://users.cs.northwestern.edu/~pdinda/Papers/sc21.pdf
---
