# Setup & Config
`uv add pre-commit --dev`

Define a pre-commit-config.yaml in project root
```
repos:
  # Ruff for linting
  - repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
    rev: v0.14.5
    hooks:
      # Run the linter.
      - id: ruff-check

  # Local hooks
  - repo: local
    hooks:
      - id: ty
        name: Type checking (ty)
        entry: uv run ty check
        language: system
        types: [python]

      - id: deptry
        name: Dependency check
        entry: uv run deptry .
        language: system
        types: [python]
        pass_filenames: false

      - id: pytest
        name: Run tests
        entry: uv run pytest
        language: system
        types: [python]

      - id: mkdocs
        name: Build documentation
        entry: uv run mkdocs build --strict
        language: system
        types: [python]
        pass_filenames: false

```


# Install and Run
In project root:
```
pre-commit install
```
Will create a
`.git/hooks/pre-commit`

Test all files 
```
pre-commit run --all-files
```

# Confirm ran
Can check output window, filter by git

```
2025-11-15 17:34:13.300 [info] > git -c user.useConfigOnly=true commit --quiet --allow-empty-message --file - [329ms]
2025-11-15 17:34:13.300 [info] Linting (ruff).......................................(no files to check)Skipped
Type checking (ty)...................................(no files to check)Skipped
Dependency checks (deptry)...........................(no files to check)Skipped
Run Python tests (pytest)............................(no files to check)Skipped
Build documentation (mkdocs).........................(no files to check)Skipped
```
