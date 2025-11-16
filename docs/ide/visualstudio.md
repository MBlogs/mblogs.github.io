IDE for editing code and projects
https://code.visualstudio.com/

### Example: user.settings
Control customisations and settings for the editor/
Invoke with:
`Cmd-Shift-P > User settings JSON`

Assumes using:
- ruff for linting
- ty for type checking (pre-release)

```json
{
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.formatOnSave": false
    },
    "python.languageServer": "None",  // Disable Pylance language server, test ty
    "terminal.integrated.defaultProfile.osx": "zsh",
    "terminal.integrated.defaultProfile.linux": "/usr/bin/zsh",
    "javascript.updateImportsOnFileMove.enabled": "always",
    "terminal.integrated.fontFamily": "MesloLGM Nerd Font",
    "jupyter.askForKernelRestart": false,
    "window.zoomLevel": 1,
    "editor.rulers": [
        {
            "column": 80,
            "color": "#ff9900"
        }
    ]
}
```