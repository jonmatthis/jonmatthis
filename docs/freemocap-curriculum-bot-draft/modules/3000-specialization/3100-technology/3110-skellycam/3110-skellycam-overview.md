---
title: "3110 - SkellyCam Overview"
module_id: "3110"
level: 3110
track: technology
---

# 3110 - SkellyCam: Overview

```{note}
SkellyCam is the camera backend for FreeMoCap, providing synchronized multi-camera video capture.
```

## Learning Objectives

- Understand SkellyCam's role in the FreeMoCap pipeline
- Learn about camera detection, configuration, and synchronization
- Explore the FastAPI/Uvicorn backend architecture

## What is SkellyCam?

SkellyCam provides:
- Multi-camera detection and management
- Synchronized video recording across multiple cameras
- Camera configuration (resolution, framerate, exposure)
- Timestamp generation for frame synchronization
- FastAPI server with React/Electron frontend

## Sub-Path Modules

| Module | Title | Focus |
|--------|-------|-------|
| 3110 | Overview | Architecture and concepts |
| 3111 | Camera Hardware | Camera detection, USB, hardware interfaces |
| 3112 | Synchronization | Timestamp systems, frame alignment |
| 3113 | Backend Architecture | FastAPI, WebSockets, multi-process design |

## Prerequisites

- Completed [3100 - Technology Track Overview](../3100-tech-overview.md)
- Python programming experience
- Basic understanding of async programming

## Deliverable

**Quiz and Bot chat**

Demonstrate understanding of SkellyCam's role and architecture.

```{seealso}
- [SkellyCam Repository](https://github.com/freemocap/skellycam)
```
