#!/bin/bash
# Temporarily store uncommited changes
git stash

# Verify correct branch
git checkout develop

# Get previous files
git fetch --all
git checkout -b master --track origin/master

# Commit
git add -A
git commit -m "Publish."

# Push
#git push origin master:master

# Restoration
git checkout develop
git branch -D master
git stash pop
