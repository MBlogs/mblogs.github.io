Ruff is a Python linter and code formatter.
It manages code formatting and highlights issues in an editing environment
(eg. Visual Studio Code)

# Useful Links
https://docs.astral.sh/ruff/installation/

# Quickstart
Add to project
```
uv add --dev ruff
```

Check linting
```
uvx ruff
```

# Configuration
https://docs.astral.sh/ruff/configuration/

Add a standalone ruff.toml file, or include direct in pyproject.toml
Ruff will understand what rules and checks it can do from this configuration file

In VSCode JSON settings:
```
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports": "explicit"
    },
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```

Example ruff config in pyproject.toml:
```toml
# ruff = Linting and formatting tool
[tool.ruff]
line-length = 88

[tool.ruff.lint]
# Error code categories:
# E = pycodestyle (PEP 8), F = pyflakes, I = import sorting
select = ["E", "F", "I"]
# Ignore specific rule codes if needed (optional)
ignore = ["E501"]

# ruff formatting options
[tool.ruff.format]
quote-style = "double"
indent-style = "space"
line-ending = "lf"
```

# Integration into VS Code
Just install the extension from VS Code extension marketplace

Extension instructions:
https://github.com/astral-sh/ruff-vscode/blob/main/README.md

ruff extension on the marketplace:
https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff


