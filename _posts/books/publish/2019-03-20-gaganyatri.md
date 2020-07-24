---
layout: page
title: "Gaganyatri"
excerpt: "Voyages of a Space Farer"
modified: 2019-03-20T14:17:25-04:00
categories: books-pub
tags: [ books-pub]
---

Gaganyatri

<ul class="post-list">
{% for post in site.categories.books-ggyn %}
  <li><article><a href="{{ site.url }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span>{% if post.excerpt %} <span class="excerpt">{{ post.excerpt | remove: '\[ ... \]' | remove: '\( ... \)' | markdownify | strip_html | strip_newlines | escape_once }}</span>{% endif %}</a></article></li>
{% endfor %}
</ul>


* Amazon Ebook [buy kindle book](https://amzn.to/312nYzJ)
