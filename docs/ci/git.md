# Commands: Common
|Command|Description|
|-|-|
|`git status`|Status of working tree|
|`git add -A`|Stage all changes|
|`git commit -m "Initial commit"`|Commit staged changes|
|`git branch`|Status of branches|
|`git checkout -b dev`|Create and checkout local branch called dev|
|`git merge dev`|Merge branch (dev) into current|
|`git init`|Initialise git repo|
|||


# Create New
1. Creates .git repo
`git init`
2. Stage everything
`git add -A`
3. Perform the commit 
`git commit -m "Initial commit"`
4. Create and push to origin
`git remote add origin git@github.com:MBlogs/pybase.git`
5. Push and set upstream
`git push -u origin main`


# Global
1. Change default branch name
`git config --global init.defaultBranch main`
2. Change username
`git config --global user.name "Your Name"`
3. Change email
`git config --global user.email your@email.com`

### .gitignore
```
*.DS_Store

# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv
.python-version
```

