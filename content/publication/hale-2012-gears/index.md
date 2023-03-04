---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Shifting GEARS to Enable Guest-context Virtual Services
subtitle: ''
summary: ''
authors:
- admin
- Lei Xia
- Peter A. Dinda
tags:
- code transformation
- virtual machines
- services
categories: []
date: '2012-09-01'
lastmod: 2023-03-03T15:14:27-06:00
featured: false
draft: false
venue: ICAC '12

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
publishDate: '2023-03-03T21:14:27.192499Z'
publication_types:
- '1'
abstract: We argue that the implementation of VMM-based virtual services for a guest
  should extend into the guest itself, even without its cooperation. Placing service
  components directly into the guest OS or application can reduce implementation complexity
  and increase performance. In this paper we show that the set of tools in a VMM required
  to enable a broad range of such guest-context services is fairly small. Further,
  we outline and evaluate these tools and describe their design and implementation
  in the context of Guest Examination and Revision Services (GEARS), a new framework
  within the Palacios VMM. We then describe two example GEARS-based services---an
  MPI communication accelerator and an overlay networking accelerator---that illustrate
  the benefits of allowing virtual service implementations to span across the VMM,
  guest, and application. Other VMMs could employ the ideas and tools in GEARS.
publication: '*Proceedings of the 9th International Conference on Autonomic Computing*'
doi: 10.1145/2371536.2371542
links:
- name: URL
  url: https://doi.org/10.1145/2371536.2371542
---
