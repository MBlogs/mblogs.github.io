https://docs.github.com/en/actions/get-started/quickstart

Create a github actions yaml 
Makes new folder and file;
At: `.github/workflows/github-actions.yml`

# Python Example
```
name: CI

on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  ci:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v5   

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install uv
        run: pip install uv

      - name: Create virtual environment
        run: uv venv .venv

      - name: Add venv to PATH
        run: echo "$(pwd)/.venv/bin" >> $GITHUB_PATH

      - name: Install dependencies (uv sync)
        run: uv sync

      - name: Lint (ruff)
        run: ruff check

      - name: Type-check
        run: ty check

      - name: Dependency check
        run: deptry .

      - name: Run tests
        run: pytest

      - name: Build docs
        run: mkdocs build

```


# Demo
```
name: GitHub Actions Demo
run-name: ${{ github.actor }} is testing out GitHub Actions 🚀
on: [push]
jobs:
  Explore-GitHub-Actions:
    runs-on: ubuntu-latest
    steps:
      - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event."
      - run: echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
      - run: echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."
      - name: Check out repository code
        uses: actions/checkout@v5
      - run: echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
      - run: echo "🖥️ The workflow is now ready to test your code on the runner."
      - name: List files in the repository
        run: |
          ls ${{ github.workspace }}
      - run: echo "🍏 This job's status is ${{ job.status }}."
```