# Git & GitHub Tutorial: Step-by-Step Guide

This guide explains how to upload a local project to GitHub using Git on Windows, fix common errors, and push future updates.

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Open Your Project Directory](#2-open-your-project-directory)
3. [Configure Git Identity](#3-configure-git-identity)
4. [Initialize Git](#4-initialize-git)
5. [Create a GitHub Repository](#5-create-a-github-repository)
6. [Connect Your Local Repository](#6-connect-your-local-repository)
7. [Commit and Push Your Code](#7-commit-and-push-your-code)
8. [Push Future Updates](#8-push-future-updates)
9. [Common Errors and Fixes](#9-common-errors-and-fixes)

---

## 1. Prerequisites

Install Git for Windows if it is not already installed.

- Download: https://git-scm.com/downloads
- Create or sign in to your GitHub account: https://github.com/

Verify Git is installed by opening Command Prompt and running:

```bash
git --version
```

If Git is installed, the command displays its version.

## 2. Open Your Project Directory

Open Command Prompt (`cmd`) and navigate to your project folder.

Example:

```bat
cd "C:\Users\YourUsername\Desktop\MyProject"
```

Replace the example path with your actual project directory.

**Important:** Run Git commands from the directory you actually want to upload.

If you upload a parent folder containing multiple projects, Git may upload all of them. For most development work, it is better to maintain a separate GitHub repository for each independent project.

## 3. Configure Git Identity

Git records an author name and email address on each commit.

Configure your name:

```bash
git config --global user.name "Your Name"
```

Configure your email:

```bash
git config --global user.email "your-email@example.com"
```

Use the name you want displayed on your commits.

### Protect Your Email Privacy

If your GitHub account blocks publishing your personal email, use your GitHub-provided `noreply` email.

1. Open https://github.com/settings/emails
2. Find your GitHub `noreply` email address.
3. Configure Git to use that exact address:

```bash
git config --global user.email "YOUR-NOREPLY-EMAIL"
```

Verify your settings:

```bash
git config --global user.name
git config --global user.email
```

The `--global` flag applies these settings to all your local repositories for your Windows user account. Omit it if you want to configure only the current repository.

## 4. Initialize Git

First, check whether your project is already a Git repository:

```bash
git status
```

If Git reports that the directory is not a repository, initialize it:

```bash
git init
```

Check the repository status:

```bash
git status
```

Stage your project files:

```bash
git add .
```

Create your first commit:

```bash
git commit -m "Initial commit"
```

If Git reports that your author identity is unknown, return to Step 3.

### Set the Main Branch

Set the branch name to `main`:

```bash
git branch -M main
```

If you run `git branch` before creating your first commit, it may show no branches. That is normal for a newly initialized repository without commits.

## 5. Create a GitHub Repository

1. Visit https://github.com/new
2. Enter a repository name, such as `MyProject`.
3. Select Public or Private.
4. If you already have local project files, leave **Add a README file** unchecked to avoid an unnecessary initial-history conflict.
5. Click **Create repository**.

Make sure you create the repository under the correct GitHub account or organization.

## 6. Connect Your Local Repository

Copy the HTTPS URL from your new GitHub repository's **Code** button.

It should resemble:

```text
https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Connect your local repository to GitHub:

```bash
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

If `origin` already exists, update it instead:

```bash
git remote set-url origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Verify the remote:

```bash
git remote -v
```

You should see the correct repository URL for both fetch and push.

### Test Repository Access

Run:

```bash
git ls-remote origin
```

If it returns references or exits successfully without output, Git can access the repository. An empty result can be normal when the remote repository has no commits yet.

If you receive `Repository not found`, verify:

- The owner or organization name.
- The exact repository name and spelling.
- That you are signed in with an account that has access.
- That your saved Git credentials belong to the correct account.

A private repository may return the same error if your credentials do not have permission to access it.

## 7. Commit and Push Your Code

Once your files are committed, push the `main` branch to GitHub:

```bash
git push -u origin main
```

The `-u` flag establishes the upstream relationship between your local `main` branch and the remote `origin/main` branch.

After a successful push, open your GitHub repository and refresh the page to see your files.

### If You Have Not Committed Yet

Run:

```bash
git add .
git commit -m "Initial commit"
git push -u origin main
```

If you already have a commit, you do not need to create another one just to push it.

## 8. Push Future Updates

After modifying your project, use this workflow:

```bash
git add .
git commit -m "Describe your changes"
git push
```

For example:

```bash
git add .
git commit -m "Improve heart drawing performance"
git push
```

### What Each Command Does

| Command | Purpose |
|---|---|
| `git add .` | Stages changes in the current directory. |
| `git commit -m "Message"` | Records a snapshot of staged changes. |
| `git push` | Uploads local commits to the configured remote. |
| `git pull` | Fetches and integrates remote changes. |
| `git status` | Shows changed, staged, and untracked files. |
| `git log --oneline` | Displays recent commits. |
| `git remote -v` | Displays remote repository URLs. |

Review `git status` before staging if you do not want every changed file included.

**Security tip:** Never commit passwords, API keys, access tokens, private keys, or other secrets. Add sensitive local files to `.gitignore` before staging them.

## 9. Common Errors and Fixes

### Error: `src refspec main does not match any`

**Cause:** The local `main` branch may not exist yet, often because no commit has been created.

**Fix:**

```bash
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

If a commit already exists, you can skip the commit command.

### Error: `Author identity unknown`

**Cause:** Git does not know which author name and email to attach to commits.

**Fix:**

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Then retry the commit.

### Error: `Repository not found`

**Cause:** The remote URL may be incorrect, the repository may not exist at that URL, or your authenticated account may lack access.

**Fix:**

```bash
git remote -v
git remote set-url origin https://github.com/OWNER/REPOSITORY.git
git ls-remote origin
```

Replace the example URL with the exact HTTPS URL copied from your repository's **Code** menu.

### Error: `GH007: Your push would publish a private email address`

**Cause:** GitHub's email privacy protection rejected the commit because its author email conflicts with your privacy settings.

**Fix:**

1. Find your `noreply` email at https://github.com/settings/emails
2. Update Git's email:

```bash
git config --global user.email "YOUR-NOREPLY-EMAIL"
```

3. If the rejected commit is your most recent commit and has not been pushed, update its author information:

```bash
git commit --amend --reset-author --no-edit
```

4. Retry:

```bash
git push -u origin main
```

This updates the most recent commit's author information while preserving its message and file contents. If the rejected push contained multiple commits, other commits may also need their author information corrected.

### Error: `remote origin already exists`

**Cause:** A remote named `origin` is already configured.

**Fix:**

```bash
git remote set-url origin https://github.com/OWNER/REPOSITORY.git
```

### Error: `nothing to commit, working tree clean`

**Meaning:** There are no new changes for Git to commit.

If your commits have not been pushed yet, run:

```bash
git push -u origin main
```

If there are no unpushed commits, your local and remote repositories may already be synchronized.

---

## Quick Reference: New Repository

Use this checklist when uploading a new local project.

- [ ] Navigate to the correct project directory.
- [ ] Configure Git name and email.
- [ ] Initialize Git if needed.
- [ ] Stage and commit the project.
- [ ] Create the GitHub repository.
- [ ] Add the correct remote URL.
- [ ] Set the branch to `main`.
- [ ] Push with `git push -u origin main`.
- [ ] Verify the files appear on GitHub.

## Quick Reference: Existing Repository

For ordinary updates:

```bash
git status
git add .
git commit -m "Describe your changes"
git push
```

**Remember:** Git stores your local history; GitHub hosts the remote repository. A successful commit does not automatically upload your code. You must push your commits to publish them on GitHub.

