---
title: "3100 - Technology Track Overview"
module_id: "3100"
level: 3100
track: technology
---

# 3100 - Technology Track: Overview

```{note}
This track focuses on the technical architecture of FreeMoCap and its component "sub-skelly" systems.
```

## Learning Objectives

- Understand the overall FreeMoCap software architecture
- Learn how the different "sub-skelly" components work together
- Prepare to dive deep into specific technical components

## The Sub-Skelly Architecture

FreeMoCap is built from several modular components, each handling a specific aspect of the motion capture pipeline:

| Component | Repository | Description |
|-----------|------------|-------------|
| **FreeMoCap Core** | `freemocap/freemocap` | Main application orchestrating the pipeline |
| **SkellyCam** | `freemocap/skellycam` | Camera backend for synchronized video capture |
| **SkellyTracker** | `freemocap/skellytracker` | Pose estimation and tracking |
| **SkellyForge** | `freemocap/skellyforge` | Data post-processing and filtering |
| **SkellyBlender** | `freemocap/freemocap_blender_addon` | Blender integration and visualization |

## Technology Sub-Paths

Choose one or more sub-paths to specialize in:

| Sub-Path | Modules | Focus |
|----------|---------|-------|
| [311x: SkellyCam](./3110-skellycam/3110-skellycam-overview.md) | 3110-3113 | Camera systems, synchronization, video capture |
| [312x: SkellyTracker](./3120-skellytracker/3120-skellytracker-overview.md) | 3120-3123 | Pose estimation, computer vision, tracking |
| [313x: SkellyForge](./3130-skellyforge/3130-skellyforge-overview.md) | 3130-3133 | Data processing, filtering, triangulation |
| [314x: SkellyBlender](./3140-skellyblender/3140-skellyblender-overview.md) | 3140-3143 | Blender addon, armatures, animation |
| [315x: FreeMoCap Core](./3150-freemocap-core/3150-core-overview.md) | 3150-3153 | Main application, GUI, pipeline orchestration |

## Prerequisites

- Completed [3000 - Specialization Overview](../3000-overview.md)
- Programming experience (Python required, TypeScript helpful)
- Interest in software development and open-source contribution

## Deliverable

**Quiz and Bot chat**

Demonstrate understanding of the overall FreeMoCap architecture and how components interact.

```{seealso}
- [FreeMoCap GitHub Organization](https://github.com/freemocap)
- [FreeMoCap Documentation](https://freemocap.github.io/documentation/)
```
