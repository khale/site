---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Extremely Fine-grained Parallelism via Scalable Concurrent Queues on Modern
  Many-core Architectures
subtitle: ''
summary: ''
authors:
- Poornima Nookala
- Peter Dinda
- admin
- Kyle Chard
- Ioan Raicu
tags: []
categories: []
date: '2021-11-01'
lastmod: 2023-03-03T14:54:07-06:00
featured: false
draft: false
venue: MASCOTS '21

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
publishDate: '2023-03-03T20:54:07.162564Z'
publication_types:
- '1'
abstract: Enabling efficient fine-grained task parallelism is a significant challenge
  for hardware platforms with increasingly many cores. Existing techniques do not
  scale to hundreds of threads due to the high cost of synchronization in concurrent
  data structures. To overcome these limitations we present XQueue, a novel lock-less
  concurrent queuing system with relaxed ordering semantics that is geared towards
  realizing scalability up to hundreds of concurrent threads. We demonstrate the scalability
  of XQueue using microbenchmarks and show that XQueue can deliver concurrent operations
  with latencies as low as 110 cycles at scales of up to 192 cores (up to 6900× improvement
  compared to traditional synchronization mechanisms) across our diverse hardware,
  including x86, ARM, and Power9. The reduced latency allows XQueue to provide orders
  of magnitude (3300×) better throughput that existing techniques. To evaluate the
  real-world benefits of XQueue, we integrated XQueue with LLVM OpenMP and evaluated
  five unmodified benchmarks from the Barcelona OpenMP Task Suite (BOTS) as well as
  a graph traversal benchmark from the GAP benchmark suite. We compared the XQueue-enabled
  LLVM OpenMP implementation with the native LLVM and GNU OpenMP versions. Using fine-grained
  task workloads, XQueue can deliver 4× to 6× speedup compared to native GNU OpenMP
  and LLVM OpenMP in many cases, with speedups as high as 116× in some cases.
publication: '*Proceedings of the 28th IEEE International Symposium on the Modeling,
  Analysis, and Simulation of Computer and Telecommunication Systems*'
links:
- name: DOI
  icon_pack: ai
  icon: doi
  url: https://dx.doi.org/10.1109/MASCOTS53633.2021.9614292
- name: IEEE
  icon_pack: ai
  icon: ieee
  url: https://ieeexplore.ieee.org/document/9614292
- name: PDF
  icon_pack: fas
  icon: file-pdf
  url: http://pdinda.org/Papers/mascots21.pdf
---
