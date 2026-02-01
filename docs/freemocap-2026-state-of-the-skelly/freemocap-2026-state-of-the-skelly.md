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
    padding-bottom: 180px;
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
  
  footer {
    font-family: 'Dosis', sans-serif;
    font-weight: 200;
    color: var(--light-cyan);
    opacity: 0.7;
    left: 0;
    right: 0;
    width: 100%;
    text-align: center;
  }
footer: State of the Skelly - 2026-02-03 | Jonathan Samir Matthis |  FreeMoCap Foundation 501(c)3
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

![w:200 center](skelly-logo.png)

# 2026 State of the Skelly Address

## FreeMoCap Foundation

*Start: 6:30 PM | Talk: 45-60 min | Q&A to follow*

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

# An Abbreviated History

![bg right:35% contain opacity:0.2](skelly-logo.png)

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

- **2021** — Ut enim ad minim veniam, quis nostrud
- **2022** — Exercitation ullamco laboris nisi ut aliquip
- **2023** — Duis aute irure dolor in reprehenderit
- **2024** — Excepteur sint occaecat cupidatat non proident
- **2025** — Sunt in culpa qui officia deserunt mollit

---

<!-- _class: title -->

# Part II
## Current State

---

# By the Numbers

| Metric | Count |
|--------|-------|
| ⭐ GitHub Stars | X,XXX |
| 💬 Discord Members | X,XXX |
| 🌍 Global Users | XX,XXX |
| 🗺️ Countries Reached | XXX |

![bg right:40% contain opacity:0.15](skelly-logo.png)

Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod.

---

# Financials

> *"Kinda loosey on specifics"*

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation.

### Estimated Burn-Down Cliff

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

![bg right:35% contain opacity:0.15](skelly-logo.png)

---

# Clients

### Current Research Partners

- 🐹 **Ferrets** — Lorem ipsum dolor sit amet
- 🐭 **Mice** — Consectetur adipiscing elit

![bg right:40% contain opacity:0.2](skelly-logo.png)

---

# 💰 Have Money? Let's Talk!

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.

**Contact us if you have funding for:**
- Research collaborations
- Custom development
- Enterprise support

![bg right:35% contain opacity:0.15](skelly-logo.png)

---

<!-- _class: title -->

# Part III
## Future Plans

---

# v2 Transition 🚀

![bg right:40% contain opacity:0.15](skellycam-logo.png)

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

### Realtime Demo

Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

### Release Plan

- **Alpha** → Ut enim ad minim veniam
- **Beta** → Quis nostrud exercitation
- **Full Release** → Ullamco laboris nisi

---

# Data Model Plans

### SkEP #1: Tidy Data + Parquet

| Current | Future |
|---------|--------|
| Lorem ipsum | Tidy format |
| Dolor sit | Parquet files |
| Amet consectetur | Standardized schema |

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum.

![bg right:35% contain opacity:0.15](skelly-logo.png)

---

# UI Transition Plan

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.

- Excepteur sint occaecat cupidatat
- Non proident sunt in culpa
- Qui officia deserunt mollit anim

![bg right:40% contain opacity:0.15](skellycam-logo.png)

---

# FMCU — FreeMoCap Curriculum

### Docs Overhaul

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

### Microcertifications 🎓

- Sed do eiusmod tempor
- Incididunt ut labore
- Et dolore magna aliqua

![bg right:35% contain opacity:0.15](skelly-logo.png)

---

# SkellyShop 🛒

### Phase 1: Charuco Boards

- With cheatsheet included!
- Lorem ipsum dolor sit amet

### Phase 2: Cameras & More

- Consectetur adipiscing elit
- Sed do eiusmod tempor

![bg right:40% contain opacity:0.2](skellycam-logo.png)

---

# FDA 510(k) Certification

### Validation Project

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

### Aaron's Dissertation 📚

Completion unlocks FDA certification pathway!

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore.

![bg right:35% contain opacity:0.15](skelly-logo.png)

---

# Blender Addon

### Rebranding

`FreeMoCap Blender Addon` → **SkellyBlender**

### Official Distribution

🎯 Goal: Get listed on Blender's official addon page

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

![bg right:35% contain opacity:0.15](skelly-logo.png)

---

<!-- _class: title -->
<!-- _footer: "" -->

![w:180 center](skelly-logo.png)

# Thank You!

## Questions?

🌐 freemocap.org | 💻 github.com/freemocap | 💬 discord.gg/freemocap

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