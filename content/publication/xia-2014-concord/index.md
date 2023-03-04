---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'ConCORD: Easily Exploiting Memory Content Redundancy through the Content-Aware
  Service Command'
subtitle: ''
summary: ''
authors:
- Lei Xia
- admin
- Peter Dinda
tags:
- content sharing
- hpc
- memory deduplication
- virtualization
categories: []
date: '2014-06-01'
lastmod: 2023-03-03T14:54:07-06:00
featured: false
draft: false
venue: HPDC '14

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
publishDate: '2023-03-03T20:54:07.811669Z'
publication_types:
- '1'
abstract: We argue that memory content-tracking across the nodes of a parallel machine
  should be factored into a distinct platform service on top of which application
  services can be built. ConCORD is a proof-of-concept system that we have developed
  and evaluated to test this claim. Our core insight is that many application services
  can be described as a query over memory content. This insight leads to a core concept
  in ConCORD, the content-aware service command architecture, in which an application
  service is implemented as a parametrization of a single general query that ConCORD
  knows how to execute well. ConCORD dynamically adapts the execution of the query
  to the amount of redundancy available and other factors. We show that a complex
  application service (collective checkpointing) can be implemented in only hundreds
  of lines of code within ConCORD, while performing well.
publication: '*Proceedings of the 23rd International Symposium on High-Performance
  Parallel and Distributed Computing*'
doi: 10.1145/2600212.2600214
links:
- name: URL
  url: https://doi.org/10.1145/2600212.2600214
---
