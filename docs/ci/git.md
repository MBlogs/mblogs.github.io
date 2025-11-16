# Commands: Common
|Command|Description|
|-|-|
|`git status`|Status of working tree|
|`git add -A`|Stage all changes|
|`git commit -m "Initial commit"`|Commit staged changes|
|`git branch`|Status of branches|
|`git checkout -b dev`|Create and checkout local branch called dev|
|`git merge dev`|Merge branch (dev) into current|
|||
|||
|||
|||

# Commands: Advanced
|Command|Description|
|-|-|
|`git init`|Initialise git repo|
|||
|||
|||
|||
|`git commit --amend --reset-author`|Ammend a previous commit (reset author)|

# Create New
1. Creates .git repo
`git init`
2. Add anything to .gitignore to not commit
`touch .gitignore`
3. Stage everything
`git add -A`
4. Commit everything
`git commit m "Initial commit"`
5. Create and push to origin
`git remote add origin git@github.com:MBlogs/pybase.git`
6. Push and set upstream
`git push -u origin main`

# Branching
1. Create new branch




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

