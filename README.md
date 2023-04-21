# Chess-with-Friends

https://chess-with-friends.atlassian.net/jira/software/projects/CWF/boards/1

Within link above we can create/track tasks

## Creating task on Jira

Select 'Board' --> 'Create' --> Add 'Summary' --> Select 'Assignee' --> 'Create'
Click on Card --> 'Create branch' --> 'Select a repository' --> 'Branch from' --> 'Create branch'

Best practice to create branch when adding features/remediating problems (even if its tiny fix), then submit PR for merge back into development/main

## Submitting PRs

Ideally we'd want 1 human approval before a PR is merged. Our github actions (CICD pipeline) can also run checks against the code (lint/sast/build/run/deploy/etc.)

git add examplefile.py
git add --all (adds all files changed)
git commit -m "message"
git push

(on github select compare & pull request)

If you want to add changes from another branch into your code before submitting PR, the following may be of use:

https://www.atlassian.com/git/tutorials/merging-vs-rebasing

Example using feature1 branch and development
git checkout development
git pull
git checkout feature1
git merge development
(this will merge changes from development into your local feature1 branch you were working on)

Same can be achieved with rebase
git checkout feature1
git fetch
git rebase development

Difference between these two sequences is the way they combine the changes: the first one uses a merge, creating a non-linear commit history, while the second one uses a rebase, creating a linear commit history.
