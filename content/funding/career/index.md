---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "CAREER: Colony: A Framework for Bespoke Virtual Execution Contexts"
summary: ""
authors: [admin]
tags: [os, virt, ds, compilers]
categories: []
date: 2023-03-10

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---
CNS Award [CNS-2239757](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2239757&HistoricalAwards=false);
$249,771; May 2023 through April 2028.

Vulnerabilities present in software running on shared computing infrastructure (e.g., cloud datacenters) can result in significant economic losses, compromised user data, and weakened national security when such infrastructure does not properly separate programs from one another in secure, isolated compartments. While techniques do exist to ensure such isolation, they typically increase the engineering burden on programmers or trade off performance for security, limiting their effectiveness and reach. Today, programmers are deploying code on shared computing infrastructure in increasingly fine-grained units (e.g., serverless computing), making this trade off more severe over time. The off-the-shelf technologies, such as containers, that isolation frameworks are often built on were not designed for this fine-grained use case. This project thus aims to ensure both performance and security for code running on cloud infrastructure by designing new isolation mechanisms from the ground up using novel operating system, compiler, programming language, and virtualization technologies. The project will help produce more robust cloud computing infrastructure that is less susceptible to attack, less likely to leak sensitive user data, and more productive for programmers. If successful, potential impacts include reduced economic losses from compromised infrastructure, strengthened national security, and increased privacy for the broader public using cloud services. The project will also make contributions in education and broadening participation in the computing profession by enhancing educational content, injecting industry-relevant and applied content into the curriculum, increasing the representation of people from diverse backgrounds in computer systems research, revitalizing the computer systems curriculum at the PI’s institution, and fostering undergraduate research engagement.

This project proposes Colony, a new software framework for lightweight, bespoke, virtualized execution contexts. Colony leverages novel execution abstractions customized for individual applications and designed for both performance and isolation. Colony contexts are synthesized using compiler analyses, and are exposed through a rich set of programming abstractions and programming language extensions. Colony builds on a new abstraction for isolated function execution, the virtualized subroutine, or virtine, along with an embeddable hypervisor. The goal of the Colony project is to achieve both high performance and strong isolation for individually isolated function contexts in a variety of applications. The project will explore various mechanisms to enable bespoke contexts, including virtualization mechanisms enhanced for optimized start-up performance, and programming models with novel language/compiler support. These bespoke contexts can be used for lighter-weight isolation than managed languages, giving them broad applicability to areas such as OS kernel drivers, third-party libraries, and database user-defined functions, as well as the more nascent serverless computing paradigm. The proposed work has potential to open up new lines of research in operating systems, virtualization, compilers, and system security.
