---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Modeling Speedup in Multi-OS Environments
subtitle: ''
summary: ''
authors:
- Brian Tauro
- Conghao Liu
- admin
tags: []
categories: []
date: '2019-10-01'
lastmod: 2023-03-03T14:54:07-06:00
featured: false
draft: false
venue: MASCOTS '19


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
publishDate: '2023-03-03T20:54:07.561483Z'
publication_types:
- '1'
abstract: For workloads that place strenuous demands on system software, novel operating
  system designs like unikernels, library OSes, and hybrid runtimes offer a promising
  path forward. However, while these systems can outperform general-purpose OSes,
  they have limited ability to support legacy applications. Multi-OS environments,
  where the application's execution is split between a compute plane and a data plane
  operating system, can address this challenge, but reasoning about the performance
  of applications that run in such a split execution environment is currently guided
  only by expert intuition and empirical analysis. As the level of specialization
  in system software and hardware continues to increase, there is both a pressing
  need and ripe opportunity for investigating analytical models that can predict application
  performance and guide programmers' intuition when considering multi-OS environments.
  In this paper we present such a model to place bounds on application speedup, beginning
  with a simple, intuitive formulation, and progressing to a more refined, predictive
  model. We present an analysis of the model, apply it to a diverse set of benchmarks,
  and evaluate it using a prototype measurement tool for analyzing workload characteristics
  relevant for multi-OS environments.
publication: '*Proceedings of the 27th IEEE International Symposium on the Modeling,
  Analysis, and Simulation of Computer and Telecommunication Systems*'
doi: 10.1109/MASCOTS.2019.00044
---
