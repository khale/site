---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Enabling Hybrid Parallel Runtimes Through Kernel and Virtualization Support
subtitle: ''
summary: ''
authors:
- admin
- Peter A. Dinda
tags:
- parallelism
- operating systems
- runtime systems
categories: []
date: '2016-07-01'
lastmod: 2023-03-03T14:54:06-06:00
featured: false
draft: false
venue: VEE '16

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
publishDate: '2023-03-03T20:54:06.212903Z'
publication_types:
- '1'
abstract: In our hybrid runtime (HRT) model, a parallel runtime system and the application
  are together transformed into a specialized OS kernel that operates entirely in
  kernel mode and can thus implement exactly its desired abstractions on top of fully
  privileged hardware access. We describe the design and implementation of two new
  tools that support the HRT model. The first, the Nautilus Aerokernel, is a kernel
  framework specifically designed to enable HRTs for x64 and Xeon Phi hardware. Aerokernel
  primitives are specialized for HRT creation and thus can operate much faster, up
  to two orders of magnitude faster, than related primitives in Linux. Aerokernel
  primitives also exhibit much lower variance in their performance, an important consideration
  for some forms of parallelism. We have realized several prototype HRTs, including
  one based on the Legion runtime, and we provide application macrobenchmark numbers
  for our Legion HRT. The second tool, the hybrid virtual machine (HVM), is an extension
  to the Palacios virtual machine monitor that allows a single virtual machine to
  simultaneously support a traditional OS and software stack alongside an HRT with
  specialized hardware access. The HRT can be booted in a time comparable to a Linux
  user process startup, and functions in the HRT, which operate over the user process's
  memory, can be invoked by the process with latencies not much higher than those
  of a function call.
publication: '*Proceedings of The12th ACM SIGPLAN/SIGOPS International Conference
  on Virtual Execution Environments*'
links:
- name: DOI
  icon_pack: ai
  icon: doi
  url: https://doi.org/10.1145/2892242.2892255
- name: ACM
  icon_pack: ai
  icon: acmdl
  url: https://dl.acm.org/doi/abs/10.1145/3007611.2892255
---
