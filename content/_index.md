---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: v1/about
    id: about
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      # Override your bio text from `authors/admin/_index.md`?
      text:
  - block: collection
    id: pubs
    content:
      title: Recent Papers
      count: 10
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      columns: '2'
      view: community/mycompact
  - block: collection
    id: news
    content:
      title: News
      subtitle: ''
      text: ''
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        folders:
          - news
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: compact
      columns: '2'
  - block: collection
    id: teaching
    content:
        title: Teaching
        filters:
            folders:
                - teaching
    design:
        columns: '2'
        view: 2
  - block: collection
    id: funding
    content:
        title: Funding
        filters:
            folders:
                - funding
    design:
        columns: '2'
        view: 2
---
