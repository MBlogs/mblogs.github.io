This project helps understand the various tools and files you see 
in typical Python projects

Python tooling is being released and updated all the time.
It can be confusing.
Especially random config .yaml files without understanding what on earth they do.

# Where to go?
Head over to docs/ folder. There are markdown files there covering many topics.

# Install this project
If wanting to try out some of the tools, you can install this project
```bash
uv sync
uv run pybase-explainer/main.py
```

# Python Tool Commands
All to be run from inside the Python .venv first
```bash
source .venv/bin/activate
```

Linting and formatting
```bash
ruff check 
```
Type checking
```bash
ty check
```
Dependency checking
```bash
deptry .
```
Run python tests
```bash
pytest
```
Generate documentation
```bash
mkdocs serve  
```

# Continuous Integration
The above checks are ran as a pre-commit hook.
To trigger manually:
```bash
pre-commit run --all-files
```
Github actions set to manual invoke only.
Can add to automatically on push in: 
```
.github/workflows/github-actions.yaml
```