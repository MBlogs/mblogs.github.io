https://docs.github.com/en/actions/get-started/quickstart

Github actions run code upon certain git actions
Such as pushing to main branch.

Executes according to a github actions configuration yaml file
For example at: `.github/workflows/github-actions.yml`


# Example: Basic demo github-actions.yml
```yaml
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

# Example: Python github-actions.yml
```yaml
name: CI

on:
  push:
    branches: [ main ]      # Deploy automatically on all commits to main
  workflow_dispatch:         # Still allows manual runs

permissions:
  contents: read
  pages: write
  id-token: write

# Allow only one concurrent deployment
concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
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

      - name: Install dependencies
        run: uv sync

      - name: Install project (editable mode)
        run: uv pip install -e .

      # Optional — remove if you fully trust pre-commit tests
      # - name: Run tests
      #   run: uv run pytest

      - name: Build docs (strict)
        run: uv run mkdocs build --strict

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./site

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

