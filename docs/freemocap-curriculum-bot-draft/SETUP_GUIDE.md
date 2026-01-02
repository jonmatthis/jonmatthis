# FreeMoCap Curriculum - MyST MD Setup Guide

**Last Updated:** December 2025  
**MyST MD Version:** 1.7.1  
**uv Version:** Latest

---

## 🚀 Quick Start

```bash
# 1. Install uv (if you don't have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Clone and enter the project
git clone https://github.com/freemocap/freemocap-curriculum.git
cd freemocap-curriculum

# 3. Sync dependencies (creates venv + installs everything)
uv sync

# 4. Run!
uv run myst start
```

That's it! Open http://localhost:3000 🎉

---

## 📦 Installation Details

### Step 1: Install uv

uv is an extremely fast Python package manager written in Rust.

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Homebrew:**
```bash
brew install uv
```

Verify:
```bash
uv --version
```

### Step 2: Clone the Project

```bash
git clone https://github.com/freemocap/freemocap-curriculum.git
cd freemocap-curriculum
```

### Step 3: Sync Dependencies

```bash
uv sync
```

This single command:
- Creates a `.venv` virtual environment
- Installs the correct Python version (if needed)
- Installs all dependencies from `pyproject.toml`
- Generates/updates `uv.lock` for reproducibility

### Step 4: Run

```bash
# Start MyST dev server
uv run myst start

# Or with Python code execution enabled
uv run myst start --execute
```

---

## 🏃 Common Commands

```bash
# === Development ===
uv run myst start              # Dev server with hot reload
uv run myst start --execute    # Dev server + run Python code cells
uv run jupyter lab             # JupyterLab for authoring

# === Building ===
uv run myst build --html       # Build static site to _build/html/
uv run myst build --pdf        # Build PDF (requires LaTeX)

# === Maintenance ===
uv sync                        # Install/update dependencies
uv sync --upgrade              # Upgrade all dependencies
uv add <package>               # Add a new dependency
uv remove <package>            # Remove a dependency
uv run myst clean              # Clean build artifacts
```

---

## 🏗️ Project Structure

```
freemocap-curriculum/
├── pyproject.toml               # Dependencies & project config
├── uv.lock                      # Locked versions (auto-generated)
├── myst.yml                     # MyST configuration
│
├── index.md                     # Landing page
├── curriculum-map.md            # Interactive DAG visualization
│
├── modules/
│   ├── level-1/                 # Foundation modules
│   ├── level-2/                 # Core skills modules
│   └── level-3/
│       ├── developer/           # Developer track
│       ├── research/            # Research track
│       └── animation/           # Animation track
│
├── notebooks/                   # Jupyter notebooks
├── visualizations/
│   └── curriculum-dag.html      # Cytoscape DAG
│
└── _static/
    ├── images/
    └── sample-data/
```

---

## ➕ Adding Dependencies

Need another package? Just add it:

```bash
uv add plotly                    # Add to main dependencies
uv add --dev pytest              # Add to dev dependencies
uv add --optional freemocap freemocap  # Add to optional group
```

This automatically updates `pyproject.toml` and `uv.lock`.

---

## 🚀 Deployment

### GitHub Actions

The included `.github/workflows/deploy.yml` automatically:
1. Installs uv
2. Runs `uv sync`
3. Builds the site
4. Deploys to GitHub Pages

Just push to `main` and it deploys!

### Manual Deploy

```bash
# Build static site
uv run myst build --html

# Output is in _build/html/
# Upload that folder to any static host
```

---

## 🆘 Troubleshooting

### uv not found

Restart your terminal, or:
```bash
source $HOME/.local/bin/env
```

### Node.js not found

MyST auto-installs Node.js when needed:
```bash
uv run myst --version
# Say 'y' when prompted
```

### Fresh start

```bash
rm -rf .venv uv.lock
uv sync
```

### Clear caches

```bash
uv cache clean
uv run myst clean --all
```

---

## 📚 Resources

- **uv Docs:** https://docs.astral.sh/uv/
- **MyST Docs:** https://mystmd.org/guide
- **FreeMoCap:** https://freemocap.org

---

Happy building! 🦴
