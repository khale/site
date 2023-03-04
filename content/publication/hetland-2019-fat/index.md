---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Prospects for Functional Address Translation
subtitle: ''
summary: ''
authors:
- Conor Hetland
- Georgios Tziantzioulis
- Brian Suchy
- admin
- Nikos Hardavellas
- Peter Dinda
tags: []
categories: []
date: '2019-10-01'
lastmod: 2023-03-04T13:08:41-06:00
featured: false
draft: false
venue: MASCOTS '19

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
publishDate: '2023-03-04T19:08:41.507366Z'
publication_types:
- '1'
abstract: Address translation fundamentally embodies a translation function that maps
  from virtual to physical addresses. In current systems, the translation function
  is encoded by the kernel in an in-memory radix tree structure (the page table hierarchy)
  which is then interpreted by the hardware (the pagewalker, pagewalk-caches, and
  TLBs). We consider implementing the translation function itself as reconfigurable
  hardware-does this make any sense? To study this question, we collected numerous
  in-situ Linux page tables for a wide range of workloads, including those from HPC,
  to serve as example translation functions. We then prototyped several potential
  mechanisms to implement the translation function, including inverted page tables
  with function-specific perfect hashing, translation functions directly implemented
  using Espresso-minimized PLAs, translation functions genetically-evolved in a language
  suitable for FPGA-like synthesis, and translation functions based on recovered/manufactured
  region (segment/mmap) lookup using multiplexor trees. Each mechanism was then evaluated
  using the Linux page tables, primarily for space and lookup speed. We report our
  findings and try to address the question.
publication: '*Proceedings of the 27th IEEE International Symposium on the Modeling,
  Analysis, and Simulation of Computer and Telecommunication Systems*'
links:
- name: DOI
  icon_pack: ai
  icon: doi
  url: https://dx.doi.org/10.1109/MASCOTS.2019.00047
- name: IEEE
  icon_pack: ai
  icon: ieee
  url: https://ieeexplore.ieee.org/document/8842897
- name: PDF
  icon_pack: fas
  icon: file-pdf
  url: http://pdinda.org/Papers/mascots19.pdf
---
