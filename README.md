This project helps understand the various tools and files you see 
in typical Python projects

Python tooling is being released and updated all the time. It can be confusing. 
Especially random config .yaml files without understanding what on earth they do.

#### Repository
The repository for this site exists at:

<https://github.com/MBlogs/mblogs.github.io>

- The docs/ folder contains all .md files behind all articles
- There are markdown files there of what is on the site
- You can install the project and create the site directly too


#### Install
Run the following in a terminal
1. Clone the repository (copy this into a local folder)
```bash
git clone "https://github.com/MBlogs/pybase-explainer.git"
```
2. Change directory to be inside your new folder
```bash
cd pybase-explainer
```
3. Sync to install dependencies and create .venv
```bash
uv sync
```
Make sure you have uv installed to run this
https://docs.astral.sh/uv/getting-started/installation/
4. Activate the .venv to run commands direct inside
```bash
source .venv/bin/activate
```
5. From here can test out the Python tool commands below
or host the documentation side with eg.
```bash
mkdocs serve
```
and open browser to your localhost where its being served
```
open http://127.0.0.1:8000/docs/
```
#
# Python Tool Commands
All to be run from inside the Python .venv first)
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