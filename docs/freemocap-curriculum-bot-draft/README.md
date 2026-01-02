# FreeMoCap Curriculum

[![Deploy MyST Site](https://github.com/freemocap/freemocap-curriculum/actions/workflows/deploy.yml/badge.svg)](https://github.com/freemocap/freemocap-curriculum/actions/workflows/deploy.yml)

A comprehensive learning path for markerless motion capture using [FreeMoCap](https://freemocap.org).

## 🎯 Overview

This curriculum takes you from your first recording to professional certification across three specialized tracks:

- **💻 Developer Track** - Build and extend FreeMoCap's codebase
- **🔬 Research Track** - Apply motion capture to scientific studies
- **🎬 Animation Track** - Create stunning visual content

## 🚀 Quick Start

### View the Curriculum Online

Visit: **[https://freemocap.github.io/freemocap-curriculum](https://freemocap.github.io/freemocap-curriculum)**

### Run Locally

```bash
# Clone the repository
git clone https://github.com/freemocap/freemocap-curriculum.git
cd freemocap-curriculum

# Install uv (if you don't have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync dependencies (creates venv + installs everything)
uv sync

# Start the development server
uv run myst start
```

Then open http://localhost:3000 in your browser.

## 📚 Curriculum Structure

```
Level 1: Foundation (All Tracks)
├── What is Motion Capture?
├── Hardware Setup
├── Software Installation
├── First Single-Camera Recording
└── Understanding Output Data

Level 2: Core Skills (All Tracks)
├── Multi-Camera Setup
├── Calibration Theory & Practice
├── Recording Optimization
├── Quality Assessment
└── Pipeline Mastery → 🏆 CORE CERTIFIED

Level 3: Specialization
├── 💻 Developer Track (4 modules) → 🏆 DEV SPECIALIST
├── 🔬 Research Track (4 modules) → 🏆 RESEARCH SPECIALIST
└── 🎬 Animation Track (4 modules) → 🏆 ANIMATION SPECIALIST

Level 4: Capstone Projects
├── Developer Professional
├── Research Professional
└── Animation Professional
```

## 🛠 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Adding a New Module

1. Create a new `.md` file in the appropriate `modules/` subdirectory
2. Add frontmatter with title, description, and curriculum metadata
3. Update `myst.yml` to include the new file in the TOC
4. Run `myst start` to preview your changes

## 📖 Built With

- [uv](https://docs.astral.sh/uv/) - Fast Python package manager
- [MyST MD](https://mystmd.org) - Markdown publishing toolchain
- [Cytoscape.js](https://js.cytoscape.org/) - Interactive curriculum visualization
- [JupyterLab](https://jupyter.org/) - Interactive Python examples

## 📄 License

Content: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)  
Code: [MIT](LICENSE)

## 🤝 Community

- 💬 [Discord](https://discord.gg/freemocap)
- 🐛 [GitHub Issues](https://github.com/freemocap/freemocap-curriculum/issues)
- 🎥 [YouTube](https://youtube.com/@freemocap)

---

Made with ❤️ by the [FreeMoCap](https://freemocap.org) community
