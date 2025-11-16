# What?

# Quickstart
https://pdm-project.org/en/latest/usage/project/
```
pdm init
pdm add -dG test pytest
pdm list --tree
```

# vEnv
```
eval $(pdm venv activate in-project)
```

# Files
- pyproject.toml: Readable deps
- .pdm-python: Local interpreter path
- 