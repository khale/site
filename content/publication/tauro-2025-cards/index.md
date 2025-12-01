---
title: 'CaRDS: Compiler-aided Remote Data Structures'
build:
  render: never
  list: never
  publishResources: false
date: '2025-11-01'
publishDate: '2025-11-21T20:01:35.803886Z'
authors:
- Brian R. Tauro
- Ian Dougherty
- Kyle C. Hale
publication_types:
- '1'
abstract: Far memory tiers improve memory utilization by enabling memory intensive
  applications to use idle memory from other machines over the network. Recently,
  compiler approaches to far memory have demonstrated how static analysis can be leveraged
  to automatically transform applications to make efficient use of remote memory tiers.
  However, policies in these compilers, e.g., the determination of whether objects
  should be remoted, prefetched, or evacuated are made conservatively at compile time
  or require profiling. While profiling can alleviate conservative policies, profile-guided
  systems can be expensive and may not work well for applications that have variation
  in their inputs. We propose CaRDS, system that combines both runtime and static
  analysis to determine far memory policies dynamically, at data structure granularity,
  and without profiling. CaRDS remoting policies can outperform prior automatic approaches
  by up to ∼ 2× and are within 25% of profile-guided systems when the local memory
  is highly constrained.
featured: false
venue: MEMO '25
publication: "*Proceedings of the SC '25 Workshops of the International Conference\
  \ for High Performance Computing, Networking, Storage and Analysis*"
doi: 10.1145/3731599.3767488
links:
- name: URL
  url: https://doi.org/10.1145/3731599.3767488
---

