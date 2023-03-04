---
# Documentation: https://wowchemy.com/docs/managing-content/

title: An Evaluation of Asynchronous Software Events on Modern Hardware
subtitle: ''
summary: ''
authors:
- admin
- Peter A. Dinda
tags: []
categories: []
date: '2018-09-01'
lastmod: 2023-03-03T14:54:06-06:00
featured: false
draft: false
venue: MASCOTS '18

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
publishDate: '2023-03-03T20:54:06.753485Z'
publication_types:
- '1'
abstract: Runtimes and applications that rely heavily on asynchronous event notifications
  suffer when such notifications must traverse several layers of processing in software.
  Many of these layers necessarily exist in order to support a general-purpose, portable
  kernel architecture, but they introduce considerable overheads for demanding, high-performance
  parallel runtimes and applications. Other overheads can arise from a mismatched
  event programming or system call interface. Whatever the case, the average latency
  and variance in latency of commonly used software mechanisms for event notifications
  is abysmal compared to the capabilities of the hardware, which can exhibit orders
  of magnitude lower latency. We leverage the flexibility and freedom of the previously
  proposed Hybrid Runtime (HRT) model to explore the construction of low-latency,
  asynchronous software events uninhibited by interfaces and execution models commonly
  imposed by general-purpose OSes. We propose several mechanisms in a system we call
  Nemo which employs kernel mode-only features to accelerate event notifications by
  up to 4,000 times and we provide a detailed evaluation of our implementation using
  extensive microbenchmarks. We carry out our evaluation both on a modern x64 server
  and the Intel Xeon Phi. Finally, we propose a small addition to existing interrupt
  controllers (APICs) that could push the limit of asynchronous events closer to the
  latency of the hardware cache coherence network.
publication: '*Proceedings of the 26th IEEE International Symposium on Modeling, Analysis,
  and Simulation of Computer and Telecommunication Systems*'
doi: 10.1109/MASCOTS.2018.00041
---
