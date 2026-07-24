---
layout: default
title: Keisuke Kwong - MAE Portfolio
permalink: /projects/
---

<hr style="margin: 40px 0; border: none; border-top: 1px solid #ccc;">

<h2 class="section-title">Coursework Overview</h2>

<div class="gallery-container">
<div class="project-gallery">
    {% for project in site.projects %}
      <div class="gallery-item">
        <a href="{{ project.url | relative_url }}">
          <img src="{{ project.thumbnail | relative_url }}" alt="{{ project.title }}" />
          <p>{{ project.title}}</p>
        </a>
      </div>
    {% endfor %}
</div>
</div>

<hr style="margin: 40px 0; border: none; border-top: 1px solid #ccc;">

<h2 class="section-title">AutoBoat Projects</h2>

<div class="gallery-container">
<div class="project-gallery">
    {% for project in site.projects2 %}
      <div class="gallery-item">
        <a href="{{ project.url | relative_url }}">
          <img src="{{ project.thumbnail | relative_url }}" alt="{{ project.title }}" />
          <p>{{ project.title}}</p>
        </a>
      </div>
    {% endfor %}
</div>
</div>