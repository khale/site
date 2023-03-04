---
# Documentation: https://wowchemy.com/docs/managing-content/

title: The Case for an Interwoven Parallel Hardware/Software Stack
subtitle: ''
summary: ''
authors:
- admin
- Simone Campanoni
- Nikos Hardavellas
- Peter A. Dinda
tags: []
categories: []
date: '2021-11-01'
lastmod: 2023-03-03T14:54:07-06:00
featured: false
draft: false
venue: ROSS '21

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
publishDate: '2023-03-03T20:54:07.028845Z'
publication_types:
- '1'
abstract: The layered structure of the system software stacks we use today allows
  for separation of concerns and increases portability. However, the confluence of
  widely available virtualization and hardware partitioning technology, new OS techniques,
  rapidly changing hardware, and significant advances in compiler technology together
  present a ripe opportunity for restructuring the stack, particularly to support
  effective parallel execution. We argue that there are cases where layers, particularly
  the compiler, run-time, kernel, and hardware, should be interwoven, enabling new
  optimizations and abstractions. We present four examples where we have successfully
  applied this interweaving model of system design, and we outline several lines of
  promising ongoing work.
publication: '*Proceedings of the 10th International Workshop on Runtime and Operating
  Systems for Supercomputers*'
---
