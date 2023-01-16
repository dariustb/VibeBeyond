---
layout: default
title: Using Git/Github
parent: Development
nav_order: 3
---

# Using Git/Github

![octocat gif](https://octodex.github.com/images/NUX_Octodex.gif)

This page is a breakdown of how the repo works with PR and git integrations with some suggestions on how to use it more smoothly.
{: .fs-6 .fw-300 }

## Branch protections on Github Repo
_Also available on the [settings](https://github.com/dariustb/VibeBeyond/settings/branch_protection_rules/33247465) page of the repo._

* Require a pull request before merging
    * All commits must be made to a non-protected branch and submitted via a pull request before they can be merged into a branch that matches this rule.
* Dismiss stale pull request approvals when new commits are pushed
    * New reviewable commits pushed to a matching branch will dismiss pull request review approvals.
* Require status checks to pass before merging
    * Choose which status checks must pass before branches can be merged into a branch that matches this rule. When enabled, commits must first be pushed to another branch, then merged or pushed directly to a branch that matches this rule after status checks have passed.
    * This currently only includes report-build-status.
* Require branches to be up to date before merging
    * This ensures pull requests targeting a matching branch have been tested with the latest code.
* Require deployments to succeed before merging
    * Choose which environments must be successfully deployed to before branches can be merged into a branch that matches this rule.
    * This currently only includes Vercel's preview deployment of the web application.
* Do not allow bypassing the above settings
    * The above settings will apply to administrators and custom roles with the "bypass branch protections" permission.

## Using git to make code changes

After cloning your repo, these are the steps:
1. Create a unique branch to work in
    ```sh
    git checkout -b your-unique-branch
    ```
2. Make your code changes
3. Save those changes locally (on git)
    ```sh
    git add /path/to/your/files.txt
    git commit -m "Description of code changes"
    ```
4. Once ready, push these changes online
    ```sh
    git push origin your-unique-branch
    ```
5. Go to your branch on Github's site and choose to "Compare and pull request"
    ![Compare & PR](https://i.stack.imgur.com/7yscx.png)
6. Fill in all the necessary details and create a Pull Request
7. When all the CI, unit, and deployment tests pass is when you can merge your changes.
    * If a test fails, you can't merge changes. You'll need to fix the errors in your code _a la Step 2_ and repeat the following steps until the code passes all tests.
8. After all tests are passed, you can delete the branch on the PR page.
9. Go to the main branch and pull changes to stay updated on new PR merges
    ```sh
    git checkout main
    git pull origin main
    ```
10. With all changes added in the PR and merged, delete the branch you created.
    ```sh
    git branch -D your-unique-branch
    ```