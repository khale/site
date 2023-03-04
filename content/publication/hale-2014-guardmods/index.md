---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Guarded Modules: Adaptively Extending the VMM's Privilege Into the Guest"
subtitle: ''
summary: ''
authors:
- admin
- Peter A. Dinda
tags: []
categories: []
date: '2014-06-01'
lastmod: 2023-03-03T14:54:06-06:00
featured: false
draft: false
venue: ICAC '14

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
publishDate: '2023-03-03T20:54:05.949098Z'
publication_types:
- '1'
abstract: 'When a virtual machine monitor (VMM) provides code that executes in the
  context of a guest operating system, allowing that code to have privileged access
  to specific hardware and VMM resources can enable new mechanisms to enhance functionality,
  performance, and adaptability. We present a software technique, guarded execution
  of privileged code in the guest, that allows the VMM to provide this capability,
  as well as an implementation for Linux guests in the Palacios VMM. Our system, which
  combines compile-time, link-time, and runtime techniques, provides the module developer
  with the following guarantees: (1) A kernel module will remain unmodified and it
  will acquire privilege only when untrusted code invokes it through developer-chosen,
  valid entry points with a valid stack. (2) Any execution path leaving the module
  will trigger a revocation of privilege. (3) The module has access to private memory.
  The system also provides the administrator with a secure method to bind a specific
  module with particular privileges implemented by the VMM. This lays the basis for
  guaranteeing that only trusted code in the guest can utilize special privileges.
  We give two examples of guarded Linux kernel modules: a network interface driver
  with direct access to the physical NIC and an idle loop that uses instructions not
  usually permitted in a guest, but which can be adaptively selected when no other
  virtual core shares the physical core. In both cases only the guarded module has
  these privileges.'
publication: '*Proceedings of the 11th International Conference on Autonomic Computing*'
---
