pdm stands for package dependency manager
It is an alternative to other Python dependency managers including:
- pip
- poetry
- uv

> 💡 **Opinion:** pdm vs. uv?:
>
> ```markdown
> I prefer using uv
> ```


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