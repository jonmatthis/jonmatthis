---
title: "3130 - SkellyForge Overview"
module_id: "3130"
level: 3130
track: technology
---

# 3130 - SkellyForge: Overview

```{note}
SkellyForge handles post-processing of motion capture data including filtering, interpolation, and 3D reconstruction.
```

## Learning Objectives

- Understand SkellyForge's role in the FreeMoCap pipeline
- Learn about data post-processing workflows
- Explore filtering and interpolation techniques
- Understand the GUI-based parameter tuning

## What is SkellyForge?

SkellyForge provides:
- Data filtering (butterworth, etc.)
- Gap interpolation for missing data
- 3D triangulation from 2D points
- GUI for interactive parameter tuning
- TOML-based configuration

## Sub-Path Modules

| Module | Title | Focus |
|--------|-------|-------|
| 3130 | Overview | Architecture and concepts |
| 3131 | Triangulation | Multi-view 3D reconstruction |
| 3132 | Filtering & Interpolation | Signal processing, gap filling |
| 3133 | Configuration & GUI | Parameter tuning, TOML config |

## Prerequisites

- Completed [3100 - Technology Track Overview](../3100-tech-overview.md)
- Python programming experience
- Basic signal processing concepts helpful

## Deliverable

**Quiz and Bot chat**

Demonstrate understanding of SkellyForge's role in post-processing.

```{seealso}
- [SkellyForge Repository](https://github.com/freemocap/skellyforge)
```
