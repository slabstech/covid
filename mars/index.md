---
layout: page
title: Mars
excerpt: Mission Space Travel
search_omit: true
---

My survival guide to mars

One Singular Mission for the next 5 years.

Learn, Run, Struggle, Write

Do everything Humanely Possible to Hitch a ride in the First Human Space Flight to Mars

<ul class="post-list">
{% for post in site.categories.mars %}
  <li><article><a href="{{ site.url }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span>{% if post.excerpt %} <span class="excerpt">{{ post.excerpt | remove: '\[ ... \]' | remove: '\( ... \)' | markdownify | strip_html | strip_newlines | escape_once }}</span>{% endif %}</a></article></li>
{% endfor %}
</ul>
