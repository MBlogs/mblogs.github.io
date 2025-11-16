# Useful Links: Python Project structure
https://arkalos.com/docs/structure/
https://jonathanadly.com/open-sourcing-a-python-project-the-right-way-in-2024

Can create entire project template:
https://github.com/fpgmaas/cookiecutter-uv


# Summary
- VS Code: Code editor
- uv: package, dependency, project manager
- git: version control

Python Packages
- ruff: linting, code syntax and formatting
- ty: type checking
- deptry: dependency checking
- pytest: testing
- mkdocs-material: automatic documentation generation

# tl;dr
```
source .venv/bin/activate
which python3
uvx ruff check  
uvx ty check
deptry .
pytest
mk
```

# Code Editor (IDE)
Visual Studio Code

# Project & Packages: PDM or UV
See uv or pdm. These facilitate:
1. .venv: Python runtime
2. pyproject.toml: Project definition including package depenencies
3. git: version control

# Git
Git is tool for maaging project version control.
```
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

Atlassian repo tutorial
https://www.atlassian.com/git/tutorials/setting-up-a-repository

Cheat sheet of code commands
https://git-scm.com/cheat-sheet

# Packages

### Linting (syntax checking): ruff
Syntax highliting and code format validation
See: ruff

### Type checking: ty or mypy
ty is from makers of ruff but is new

### Dependency checking: deptry
https://github.com/fpgmaas/deptry/

### Testing: pytest

### Documentation: mkdocs-material
mkdocs allows docs generation from code
mkdocs-material is  an extension to that to make it better 
`uv add mkdocs-material`

Create yml config in root
`echo "site_name: MB" >> mkdocs.yml`
Create docs folder with index.md
`mkdir docs && touch docs/index.md`
Serve
```
mkdocs serve
open http://127.0.0.1:8000
```

Build (Create directory for site)
`mkdocs build`
note: creates static site. Idea isn't to VC that.


# Code
```
mkdir src
mkdir src/myproject
touch src/myproject/__init__.py		
```

# Project folder structure
```
mypackage/
├── README.md                # Project overview
├── mkdocs.yml               # (mkdocs) config for generating docs
├── pyproject.toml           # (uv) dependencies, tool configs
├── uv.lock					          # (uv) machine dependency tracking
├── pyproject.toml           # (uv) python version
├── .gitignore               # (git) paths excluded from version control
├── .vnev                    # (venv) Python runtime
├── .python-version          # (venv) string, python version
├── .pytest_cache            # (pytest) cache from pytest
├── .ruff_cache              # (auto:ruff) cache from ruff check
├── .DS_Store                # (auto:mac) macOS for finder preferences

│
├── myproject/                     # <--- actual Python code lives here
│   ├── __init__.py
│   ├── main.py
│   ├── cli.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── tests/                   # all tests live here
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
│
├── docs/                    # documentation (MkDocs source)
│   ├── index.md
│   └── api.md
│
├── .github/                 # CI/CD workflows (GitHub Actions)
│   └── workflows/
│       └── ci.yml
│
└── scripts/                 # optional: helper scripts (e.g. data setup)
│   └── setup_env.sh
```

