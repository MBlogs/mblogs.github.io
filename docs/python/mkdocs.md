Documentation
https://squidfunk.github.io/mkdocs-material/

mkdocs is a way to generate documentation from Python code
mkdocs-material is a theme for mkdocs to add functionality and style

### Run
Generate docs. Turns markdown into a static website
`uvx mkdocs serve `
You likely need another terminal window, as hosted site takes this one.

Open http://127.0.0.1:8000 in web browser
`open http://127.0.0.1:8000`

### Quickstart
`uv add mkdocs-material`
Then in project root, make sure running in python venv
`source .venv/bin/activate`
`mkdocs serve`

Makes
`mkdocs.yml` : Confiuration file
`docs/index.md`: Documentation markdown

#### Plugins
Unlike extensions, plugins need adding to dependencies directly
`uv add 'mkdocstrings[python]`

### Write markdown file
Markdown a common way of formattting files
Special characters are used to 

### Markdown docstrings
Provided:
1. installed mkdocstrings plugin

This markdown will automatically generate docs
```docs/main.md
::: mblogs.main
```


# mkdocs.yml
Basic
```
site_name: pybase
site_description: Official documentation for My Project
site_author: Your Name

nav:
  - Home: index.md
  - Reference: api.md

markdown_extensions:
  - toc:                # Table of contents with anchors
      permalink: true
```

Advanced
```
site_name: pybase Documentation
site_url: https://example.com/docs/
site_description: A python repo base 
repo_url: https://github.com/myuser/myproject
repo_name: pybase

nav:
  - Home: index.md
  - api: api.md

theme:
  name: material # Or 'readthedocs', 'mkdocs'
  palette:
    - scheme: default
      primary: indigo
      accent: deep orange
    - scheme: slate
      primary: blue
      accent: light blue
  features:
    - search.suggest
    - search.highlight
    - content.code.annotate
    - toc.integrate


plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          options:
            docstring_style: google
     

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - attr_list
  - md_in_html
  - toc:
      permalink: true
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
```
