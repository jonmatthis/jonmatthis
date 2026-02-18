# Tauri Monaco Editor

A simple Tauri desktop app that lets you browse your local filesystem and view plaintext files in a Monaco editor.

## Prerequisites

- [Node.js](https://nodejs.org/) (v18+)
- [Rust](https://www.rust-lang.org/tools/install) (latest stable)
- Tauri CLI prerequisites for your platform:
  - **Linux**: `sudo apt install libwebkit2gtk-4.1-dev build-essential curl wget file libxdo-dev libssl-dev libayatana-appindicator3-dev librsvg2-dev`
  - **macOS**: Xcode Command Line Tools (`xcode-select --install`)
  - **Windows**: [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

## Setup

```bash
# Install dependencies
npm install

# Run in development mode
npm run tauri dev

# Build for production
npm run tauri build
```

## Features

- Browse local filesystem directories
- View plaintext files with syntax highlighting
- Monaco editor with VS Code-like experience
- Language detection based on file extension

## Supported Languages

The editor auto-detects and highlights: TypeScript, JavaScript, JSON, HTML, CSS, Markdown, Python, Rust, Go, Java, C/C++, Shell, YAML, XML, SQL, TOML, and more.
