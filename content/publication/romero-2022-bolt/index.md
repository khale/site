---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Bolt: Fast Inference for Random Forests'
subtitle: ''
summary: ''
authors:
- Eduardo Romero
- Christopher Stewart
- Angela Li
- admin
- Nathaniel Morris
tags: []
categories: []
date: '2022-10-01'
lastmod: 2023-03-03T14:58:10-06:00
featured: false
draft: false
venue: Middleware '22

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
publishDate: '2023-03-03T20:58:10.820926Z'
publication_types:
- '1'
abstract: "Random forests use ensembles of decision trees to boost accuracy for machine\
  \ learning tasks. However, large ensembles slow down inference on platforms that\
  \ process each tree in an ensemble individually. We present Bolt, a platform that\
  \ restructures whole random forests, not just individual trees, to speed up inference.\
  \ Conceptually, Bolt maps every path in each tree to a lookup table which, if cache\
  \ were large enough, would allow inference with just one memory access. When the\
  \ size of the lookup table exceeds cache capacity, Bolt employs a novel combination\
  \ of lossless compression, parameter selection, and bloom filters to shrink the\
  \ table while preserving fast inference. We compared inference speed in Bolt to\
  \ three state-of-the-art platforms: Python Scikit-Learn, Ranger, and Forest Packing.\
  \ We evaluated these platforms using datasets with vision, natural language processing\
  \ and categorical applications. We observed that on ensembles of shallow decision\
  \ trees Bolt can run 2--14X faster than competing platforms and that Bolt's speedups\
  \ persist as the number of decision trees in an ensemble increases."
publication: '*Proceedings of the 23rd ACM/IFIP International Middleware Conference*'
links:
- name: ACM
  icon_pack: ai
  icon: acmdl
  url: https://dl.acm.org/doi/10.1145/3528535.3531519
---
