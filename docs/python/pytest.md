Pytest allows writing and re-running unit and system tests on the python codebase

### Installation
https://docs.pytest.org/en/stable/getting-started.html#install-pytest

### Usage
https://docs.pytest.org/en/stable/how-to/usage.html

### Install
Usually want to add as a dev dependency group
Then store test_x.py scripts inside a tests folder
```
uv add --dev pytest
mkdir tests
```

In pyproject.toml
```python
# pytest = Testing framework configuration
[tool.pytest.ini_options]
# Version of pytest to ensure compatibility
minversion = "9.0"
# Command line options to always include when pytest run
# ra = show extra summary. q = reduce verbosity
addopts = ["-ra", "-q"]
# Lets pytest know to a folder, eg. src to sys.path
pythonpath = ["src"]
```


### Quickstart
Run test
Be sure running python environment eg,

Then
```
uvx pytest
uvx pytest tests
```
Adds .pytest_cache folder

Equivalently if not using uv; directly run in Python venv
```
source .venv/bin/activate
pytest
```

# Write a test
- Name files and functions to test within,  prefix test_ 
Example: test_main.py in tests folder in project root
```
from pybase.main import main

def test_main():
    try:
        main()
    except Exception as e:
        assert False, f"main() raised an exception: {e}"
```

