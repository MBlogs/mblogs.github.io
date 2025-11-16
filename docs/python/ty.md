Type checking
** Warning: Prerelease. Check out mypy instead for production.

https://realpython.com/python-ty/

### Install
Add to project
`uv add --dev ty`

Run:
`uvx ty check`

### Configuration
[tool.ty.rules]
index-out-of-bounds = "ignore"

### Editor
Add extension to VSCode
https://github.com/astral-sh/ty-vscode