---
title: "3120 - SkellyTracker Overview"
module_id: "3120"
level: 3120
track: technology
---

# 3120 - SkellyTracker: Overview

```{note}
SkellyTracker is the pose estimation backend for FreeMoCap, providing a unified API for multiple tracking backends.
```

## Learning Objectives

- Understand SkellyTracker's role in the FreeMoCap pipeline
- Learn about the tracker abstraction pattern
- Explore available pose estimation backends
- Understand 2D keypoint detection fundamentals

## What is SkellyTracker?

SkellyTracker provides:
- Unified API for multiple pose estimation backends
- Support for MediaPipe, YOLO, and other trackers
- BaseTracker abstract class for extensibility
- Image, video, and webcam processing
- Consistent output format across trackers

## Sub-Path Modules

| Module | Title | Focus |
|--------|-------|-------|
| 3120 | Overview | Architecture and concepts |
| 3121 | Tracker Abstraction | BaseTracker ABC, creating custom trackers |
| 3122 | Pose Estimation Models | MediaPipe, YOLO, model comparison |
| 3123 | Output Formats | Keypoint data structures, coordinate systems |

## Prerequisites

- Completed [3100 - Technology Track Overview](../3100-tech-overview.md)
- Python programming experience
- Basic understanding of computer vision concepts

## Deliverable

**Quiz and Bot chat**

Demonstrate understanding of SkellyTracker's role and the tracker abstraction pattern.

```{seealso}
- [SkellyTracker Repository](https://github.com/freemocap/skellytracker)
- [SkellyTracker on PyPI](https://pypi.org/project/skellytracker/)
```
