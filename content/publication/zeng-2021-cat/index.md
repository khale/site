---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Playing Fetch with CAT: Composing Cache Partitioning and Prefetching for Task-Based
  Query Processing'
subtitle: ''
summary: ''
authors:
- Qitian Zeng
- admin
- Boris Glavic
tags: []
categories: []
date: '2021-06-01'
lastmod: 2023-03-03T14:54:08-06:00
featured: false
draft: false
venue: DaMoN '21

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
publishDate: '2023-03-03T20:54:07.989801Z'
publication_types:
- '1'
abstract: Software prefetching and hardware-based cache allocation techniques (CAT)
  have been successfully applied in main-memory database engines to fetch data into
  cache before it is needed and to partition a shared last-level cache (LLC) to prevent
  concurrent tasks from evicting each others' data. We investigate the interaction
  of these techniques and demonstrate that while a single prefetching strategy is
  sufficient, the combination of both techniques is only effective if the cache partitioning
  strategy adapts the partitioning based on the types of tasks currently sharing an
  LLC. We present a simple, yet effective, scheme that uses prefetching and adapts
  cache partition allocations dynamically.
publication: '*Proceedings of the 17th International Workshop on Data Management on
  New Hardware (DaMoN 2021)*'
links:
- name: DOI
  icon_pack: ai
  icon: doi
  url: https://doi.org/10.1145/3465998.3466016
- name: ACM
  icon_pack: ai
  icon: acmdl
  url: https://dl.acm.org/doi/10.1145/3465998.3466016
- name: PDF
  icon_pack: fas
  icon: file-pdf
  url: http://cs.iit.edu/~dbgroup/assets/pdfpubls/ZH21.pdf
---
