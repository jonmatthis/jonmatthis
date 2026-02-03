---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Dosis:wght@200;600&family=Roboto:wght@300;400;500&display=swap');
  
  :root {
    --dark-teal: #254342;
    --medium-teal: #365d5f;
    --coral-decorative: #d95157;
    --coral-heading: #f07a7f;      /* 3.98:1 - AA large text */
    --coral-text: #ff8a8a;         /* 4.72:1 - AA normal text */
    --light-cyan: #a4d6d9;         /* 6.73:1 - AA normal text */
  }
  
  section {
    background-color: var(--dark-teal);
    color: #ffffff;
    font-family: 'Roboto', sans-serif;
    font-weight: 300;
  }
  
  h1 {
    font-family: 'Dosis', sans-serif;
    font-weight: 600;
    color: var(--light-cyan);
    letter-spacing: 0.05em;
  }
  
  h2 {
    font-family: 'Dosis', sans-serif;
    font-weight: 200;
    color: var(--coral-heading);
    letter-spacing: 0.05em;
  }
  
  h3 {
    font-family: 'Dosis', sans-serif;
    font-weight: 600;
    color: var(--light-cyan);
  }
  
  a {
    color: var(--coral-text);
  }
  
  strong {
    color: var(--coral-text);
  }
  
  code {
    background-color: var(--medium-teal);
    color: var(--light-cyan);
  }
  
  blockquote {
    border-left: 4px solid var(--coral-text);
    background-color: var(--medium-teal);
    padding: 0.5em 1em;
    color: #ffffff;
    font-style: normal;
  }
  
  blockquote em {
    color: var(--light-cyan);
    font-style: italic;
  }
  
  table {
    font-size: 0.9em;
  }
  
  th {
    background-color: var(--medium-teal);
    color: var(--light-cyan);
  }
  
  td {
    background-color: var(--light-cyan);
    color: var(--dark-teal);
  }
  
  section.title {
    text-align: center;
    justify-content: center;
    padding-bottom: 120px;
  }
  
  section.title h1 {
    font-size: 2.8em;
  }
  
  section.invert {
    background-color: var(--light-cyan);
    color: var(--dark-teal);
  }
  
  section.invert h1,
  section.invert h3 {
    color: var(--dark-teal);
  }
  
  section.invert strong,
  section.invert a {
    color: var(--dark-teal);
    font-weight: 500;
  }
  
  img[alt~="center"] {
    display: block;
    margin: 0 auto;
  }
  
  /* Section progress indicator */
  section::after {
    font-family: 'Dosis', sans-serif;
    font-size: 0.7em;
    color: var(--light-cyan);
    opacity: 0.6;
    position: absolute;
    top: 20px;
    right: 30px;
  }
  
  section.part-background::after { content: "Background"; }
  section.part-current::after { content: "Current State"; }
  section.part-future::after { content: "Future Plans"; }
  
  /* Footer styling - spread across bottom */
  footer {
    font-family: 'Dosis', sans-serif;
    font-weight: 200;
    color: var(--light-cyan);
    opacity: 0.7;
    left: 30px;
    right: 30px;
    bottom: 20px;
    width: calc(100% - 60px);
    display: flex;
    justify-content: space-between;
    text-align: center;
  }
footer: State of the Skelly 2026  ·  Jonathan Samir Matthis  ·  FreeMoCap Foundation 501(c)3
---

<!--
BUILD INSTRUCTIONS
==================
npm install -g @marp-team/marp-cli

HTML (for presenting, supports video):
  marp freemocap-2026-state-of-the-skelly.md -o slides.html --html

PDF (for sharing, no video):
  marp freemocap-2026-state-of-the-skelly.md -o slides.pdf --html --allow-local-files

Live preview:
  marp -w freemocap-2026-state-of-the-skelly.md --html

Presenting: Open HTML in browser, F=fullscreen, P=presenter view

Keep in same folder: .md, skelly-logo.png, skellycam-logo.png, *.mp4
-->

<!-- _class: title -->
<!-- _footer: "" -->

<div style="padding-top: 60px;">

![w:200 center](skelly-logo.png)

# 2026 State of the Skelly Address

## FreeMoCap Foundation

</div>

<div style="margin-top: 80px; font-size: 0.9em;">

*Start: 6:30 PM  ·  Talk: 45-60 min  ·  Q&A to follow*

</div>

---

# Agenda

1. **Background** — An abbreviated history
2. **Current State** — Numbers, financials, clients
3. **Future Plans** — v2, curriculum, shop, FDA, Blender

![bg right:40% contain opacity:0.15](skelly-logo.png)

---

<!-- _class: title -->

# Part I
## Background

---
<!-- _class: part-background -->

# 2017 — OpenPose Released

![bg right:45% contain opacity:0.9](skelly-logo.png)

<!-- Video placeholder: lab footage -->

---
<!-- _class: part-background -->

# 2019 — Northeastern

![bg right:45% contain opacity:0.9](skelly-logo.png)

<!-- Video placeholder: NEU footage -->

---
<!-- _class: part-background -->

# 2020 — COVID


![bg right:45% contain opacity:0.9](skelly-logo.png)

---
<!-- _class: part-background -->

# 2021 — First Public Post

![bg right:45% contain opacity:0.9](skelly-logo.png)

<!-- Video placeholder: first release video -->
---

<!-- _class: part-background -->

# 202? - Meowmaline

![bg right:45% contain opacity:0.9](skelly-logo.png)

<!-- Video placeholder: meowmaline -->

---
<!-- _class: part-background -->

# 2026 — Today

Where we are now - the scary cliff approaches

![bg right:45% contain opacity:0.9](skelly-logo.png)

---

<!-- _class: title -->

# Part II
## Current State

---
<!-- _class: part-current -->

# By the Numbers

| Metric | Count |
|--------|-------|
| ⭐ GitHub Stars | 4,533 |
| 💬 Discord Members | 3,387 |
| 🌐 Global Users | 10,222+ |
| 🗺️ Countries Reached | 140 |

![bg right:40% contain](freemocap-github-star-history.png)

![bg right:40% contain](freemocap-user-dashboard.png)

- A field trip to Dataland - https://freemocap.org/data.html
---
<!-- _class: part-current -->

# Financials
- Doing Ok
- Will survive past the 2026 June 30 Scary Cliff
- ...but will be thrive??
<!-- Light slide — will discuss verbally -->

![bg right:35% contain opacity:0.15](skelly-logo.png)

---
<!-- _class: part-current -->

# Clients

### Current Research Partners

- Ben Scholl - Developmental Laser Ferrets 
- DF - Mouse eye tracker and all-day Pupilometry 

![bg right:40% contain opacity:0.2](skelly-logo.png)

---
<!-- _class: part-current -->

# Now Accepting Clients

**Interested in working with us?**

- Research collaborations
- Custom development
- Enterprise support

- Support tiers

![bg right:35% contain opacity:0.15](skelly-logo.png)

---

<!-- _class: title -->

# Part III
## Future Plans

---
<!-- _class: part-future -->

# v2 Transition 🚀

![bg right:40% contain opacity:0.15](skellycam-logo.png)

### Realtime Demo

### Release Plan

- **Alpha** — Core functionality
- **Beta** — UI overhaul, testing
- **Full Release** — Production ready

---
<!-- _class: part-future -->

# Data Model Plans

### SkEP #1: Tidy Data + Parquet

| Current | Future |
|---------|--------|
| NumPy arrays | Tidy format |
| .npy files | Parquet files |
| Ad-hoc schema | Standardized schema |

![bg right:35% contain opacity:0.15](skelly-logo.png)

---
<!-- _class: part-future -->

# Documentation Overhaul

Complete docs rewrite in progress

### FreeMoCap University 🎓

Microcertifications coming

![bg right:35% contain opacity:0.15](skelly-logo.png)

---
<!-- _class: part-future -->

# SkellyShop 🛒

### Charuco Boards

Available now — print-on-demand

### Cameras

Coming soon

![bg right:40% contain opacity:0.2](skellycam-logo.png)

---
<!-- _class: part-future -->

# FreeMoCap Validation

### Aaron's Dissertation 📚

Completion unlocks next steps

### FDA 510(k) Certification

Future pathway

![bg right:35% contain opacity:0.15](skelly-logo.png)

---
<!-- _class: part-future -->

# Blender Addon

### Rebranding

`FreeMoCap Blender Addon` → **SkellyBlender**

### Official Distribution

🎯 Goal: Blender's official addon page

![bg right:35% contain opacity:0.15](skelly-logo.png)

---

<!-- _class: title -->
<!-- _footer: "" -->

![w:180 center](skelly-logo.png)

# Thank You!

## Questions?

🌐 freemocap.org  ·  💻 github.com/freemocap  ·  💬 discord.gg/freemocap

---

# Video from URL

<div style="display: flex; justify-content: center; align-items: center; height: 80%;">
  <video src="https://www.w3schools.com/html/mov_bbb.mp4" controls style="max-height: 65vh; max-width: 90%;"></video>
</div>

---

# Video from Local File (Autoplay)

<div style="display: flex; justify-content: center; align-items: center; height: 80%;">
  <video src="local_video.mp4" autoplay muted loop style="max-height: 65vh;"></video>
</div>