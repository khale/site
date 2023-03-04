---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Task Parallel Assembly Language for Uncompromising Parallelism
subtitle: ''
summary: ''
authors:
- Mike Rainey
- Ryan R. Newton
- admin
- Nikos Hardavellas
- Simone Campanoni
- Peter Dinda
- Umut A. Acar
tags:
- parallel programming languages
- granularity control
categories: []
date: '2021-01-01'
lastmod: 2023-03-04T13:00:33-06:00
featured: false
draft: false
venue: PLDI '21

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
publishDate: '2023-03-04T19:00:33.323040Z'
publication_types:
- '1'
abstract: 'Achieving parallel performance and scalability involves making compromises
  between parallel and sequential computation. If not contained, the overheads of
  parallelism can easily outweigh its benefits, sometimes by orders of magnitude.
  Today, we expect programmers to implement this compromise by optimizing their code
  manually. This process is labor intensive, requires deep expertise, and reduces
  code quality. Recent work on heartbeat scheduling shows a promising approach that
  manifests the potentially vast amounts of available, latent parallelism, at a regular
  rate, based on even beats in time. The idea is to amortize the overheads of parallelism
  over the useful work performed between the beats. Heartbeat scheduling is promising
  in theory, but the reality is complicated: it has no known practical implementation.
  In this paper, we propose a practical approach to heartbeat scheduling that involves
  equipping the assembly language with a small set of primitives. These primitives
  leverage existing kernel and hardware support for interrupts to allow parallelism
  to remain latent, until a heartbeat, when it can be manifested with low cost. Our
  Task Parallel Assembly Language (TPAL) is a compact, RISC-like assembly language.
  We specify TPAL through an abstract machine and implement the abstract machine as
  compiler transformations for C/C++ code and a specialized run-time system. We present
  an evaluation on both the Linux and the Nautilus kernels, considering a range of
  heartbeat interrupt mechanisms. The evaluation shows that TPAL can dramatically
  reduce the overheads of parallelism without compromising scalability.'
publication: '*Proceedings of the 42nd ACM SIGPLAN International Conference on Programming
  Language Design and Implementation*'
links:
- name: DOI
  icon_pack: ai
  icon: doi
  url: https://doi.org/10.1145/3453483.3460969
- name: ACM
  icon_pack: ai
  icon: acmdl
  url: https://dl.acm.org/doi/10.1145/3453483.3460969
- name: PDF
  icon_pack: fas
  icon: file-pdf
  url: https://www.andrew.cmu.edu/user/mrainey//papers/tpal-long.pdf
- name: Website
  icon_pack: fas
  icon: window-maximize
  url: https://www.andrew.cmu.edu/user/mrainey//tpal/tpal.html
- name: Code
  icon_pack: fab
  icon: github
  url: https://github.com/mikerainey/tpal
  
---
