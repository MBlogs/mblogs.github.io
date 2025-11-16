uv is a Python project management system, built in ruff and super fast
It is used in place of Python package management like poetry or pdm.

Installation:
https://docs.astral.sh/uv/getting-started/installation/

High level functionality
https://docs.astral.sh/uv/getting-started/features/

# Quickstart
Project start: https://docs.astral.sh/uv/concepts/projects/layout/
```
uv init projectname
uv venv
uv add mkdocs-material
```

### 1. uv init
Starting point, creates the folder with base files needed including:
- .gitignore: file patterns to exclude from version control. The folder is made as a git repo.
- .python-version: informs what Python version project needs to be run with
- main.py: starting point for running (main function)
- pyproject.toml: human friendly project markdown of dependencies and such
- README.md: Install instructions, what will be displayed in the repo first page too.

### 2. uv venv
- Creates a .venv virtual environment to use as the Python runtime

### 3. uv add
- Adds Python dependencies. Are added to pyproject.toml
- (on first run) Creates a uv.lock file, which is machine readable version of the dependency tree
- There is compatability/conversion to `pylock.toml`

# Managing Dependencies
Add new package to project dependency. Latest unless a version specified.
```
uv add httpx
uv add "httpx>=0.20"
uv add "httpx>0.1.0"
uv add --dev pytest
uv add --group lint ruff
```
Groups can dictate multiple packages. And note:
--dev is equivalent to --group dev

Remove package from project dependency
`uv remove`

Shows full dependency tree
`uv tree`

# Running Tools

```
uvx ruff
uv tool run ruff
```
Above are equivalent


---
### Disclaimer: 
- These articles are always informal notes to myself at the time of engaging with the tools.
- I always include the formal, dedicated tooling articles at the start.
- Those should be treated as ultimate source of truth for that tool
---