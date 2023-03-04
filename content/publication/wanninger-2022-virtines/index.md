---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Isolating Functions at the Hardware Limit with Virtines
subtitle: ''
summary: ''
authors:
- Nicholas C. Wanninger
- Joshua J. Bowden
- Kirtankumar Shetty
- Ayush Garg
- admin
tags: []
categories: []
date: '2022-01-01'
lastmod: 2023-03-03T14:54:07-06:00
featured: false
draft: false
venue: EuroSys '22
award: Best Artifact Award

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
publishDate: '2023-03-03T20:54:07.687755Z'
publication_types:
- '1'
abstract: An important class of applications, including programs that leverage third-party
  libraries, programs that use user-defined functions in databases, and serverless
  applications, benefit from isolating the execution of untrusted code at the granularity
  of individual functions or function invocations. However, existing isolation mechanisms
  were not designed for this use case; rather, they have been adapted to it. We introduce
  virtines, a new abstraction designed specifically for function granularity isolation,
  and describe how we build virtines from the ground up by pushing hardware virtualization
  to its limits. Virtines give developers fine-grained control in deciding which functions
  should run in isolated environments, and which should not. The virtine abstraction
  is a general one, and we demonstrate a prototype that adds extensions to the C language.
  We present a detailed analysis of the overheads of running individual functions
  in isolated VMs, and guided by those findings, we present Wasp, an embeddable hypervisor
  that allows programmers to easily use virtines. We describe several representative
  scenarios that employ individual function isolation, and demonstrate that virtines
  can be applied in these scenarios with only a few lines of changes to existing codebases
  and with acceptable slowdowns.
publication: '*Proceedings of the Seventeenth European Conference on Computer Systems*'
links:
- name: ACM
  icon_pack: ai
  icon: acmdl
  url: https://doi.org/10.1145/3492321.3519553
- name: arXiv
  icon_pack: ai
  icon: arxiv
  url: https://arxiv.org/abs/2104.11324
- name: Code
  icon_pack: fab
  icon: github
  url: https://github.com/virtines
- name: Reproducible Artifact
  icon_pack: ai
  icon: zenodo
  url: https://zenodo.org/record/6350453
---
