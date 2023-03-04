---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Segment Gating for Static Energy Reduction in Networks-on-Chip
subtitle: ''
summary: ''
authors:
- admin
- Boris Grot
- Stephen W. Keckler
tags: []
categories: []
date: '2009-12-01'
lastmod: 2023-03-03T14:54:05-06:00
featured: false
draft: false
venue: NoCArc '09

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
publishDate: '2023-03-03T20:54:05.815687Z'
publication_types:
- '1'
abstract: Chip multiprocessors (CMPs) have emerged as a primary vehicle for overcoming
  the limitations of uniprocessor scaling, with power constraints now representing
  a key factor of CMP design. Recent studies have shown that the on-chip interconnection
  network (NOC) can consume as much as 36% of overall chip power. To date, researchers
  have employed several techniques to reduce power consumption in the network, including
  the use of on/off links by means of power gating. However, many of these techniques
  target dynamic power, and those that consider static power focus exclusively on
  flit buffers. In this paper, we aim to reduce static power consumption through a
  comprehensive approach that targets buffers, switches, arbitration units, and links.
  We establish an optimal power-down scheme which we use as an upper bound to evaluate
  several static policies on synthetic traffic patterns. We also evaluate dynamic
  utilization-aware power-down policies using traces from the PARSEC benchmark suite.
  We show that both static and dynamic policies can greatly reduce static energy at
  low injection rates with only minimal increases in dynamic energy and latency.
publication: '*Proceedings of the 2nd International Workshop on Network on Chip Architectures*'
links:
- name: DOI
  icon_pack: ai
  icon: doi
  url: https://dx.doi.org/10.1145/1645213.1645227
- name: ACM
  icon_pack: ai
  icon: acmdl
  url: https://dl.acm.org/doi/10.1145/1645213.1645227
---
