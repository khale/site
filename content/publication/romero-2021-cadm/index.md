---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Memory Mapping and Parallelizing Random Forests for Speed and Cache Efficiency
subtitle: ''
summary: ''
authors:
- Eduardo Romero-Gainza
- Christopher Stewart
- Angela Li
- admin
- Nathaniel Morris
tags: []
categories: []
date: '2021-08-01'
lastmod: 2023-03-03T14:54:07-06:00
featured: false
draft: false
venue: PDADS '21

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
publishDate: '2023-03-03T20:54:07.421699Z'
publication_types:
- '1'
abstract: Memory mapping enhances decision tree implementations by enabling constant-time
  statistical inference, and is particularly effective when memory mapped tables fit
  in processor cache. However, memory mapping is more challenging when applied to
  random forests—ensembles of many trees—as the table sizes can easily outstrip cache
  capacity. We argue that careful system design for parallel and cache efficiency
  can make memory mapping effective for random forests. Our preliminary results show
  memory-mapped forests can speed up inference latency by a factor of up to 30 × .
publication: '*International Workshop on Parallel and Distributed Algorithms for Decision
  Sciences*'
links:
- name: DOI
  icon_pack: ai
  icon: doi
  url: 10.1145/3458744.3474052
- name: ACM
  icon_pack: ai
  icon: acmdl
  url: https://doi.org/10.1145/3458744.3474052
- name: Talk
  icon_pack: fab
  icon: youtube
  url: https://www.youtube.com/watch?v=njFgPfFqikI&t=2s
---
