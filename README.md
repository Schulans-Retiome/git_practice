# Introduction
> **Note:** this is a work in progress!

This repository serves as a practice repository to explore version control 
with git as well as programming challenges and tutorials that will be shared
within the group of people with access to this repository. The idea of having
this repository is to be able to explore the tools freely without the fear
of destroying the repository. This project is open for all levels of expertise
from beginner to experts. As such, we highly encourage to use the repository
when learning tutorials for chosen programming languages.

The goal of this project are as follows:
1. Explore git version control
2. Explore chosen programming languages
3. Share codes and programs within the group
4. Share new technology and tools within the group

## Pre-requisites
In order to start with this project, some tools and understanding of concepts
must be achieved by the user.

Tools required:
1. Git
2. Programming language pre-requisites (i.e. Python installation, GCC for C/C++, etc.)
3. IDE for chosen programming language (i.e. Pycharm for Python, VS Code or Notepad++ for C/C++)

Knowledge requirement:
1. Basic understanding of Git and version control and how to set it up and use it

## Getting started
In order to get started, once you have set up the pre-requisites, create a directory
in your drive and clone this repository into it _(either via HTTPS or SSH)_.

**HTTPS:** `https://github.com/MikoStellio/git_practice.git`  
**SSH:** `git@github.com:MikoStellio/git_practice.git`

> **Note:** if you are having issues with cloning using SSH, consider using HTTPS.

Using HTTPS might be easier for beginners, but you might want to consider learning
how to set up an SSH as it only requires a one time setup. Much more efficient and
convenient to use especially in a quick moving project.

To learn more about SSH setup, check this tutorial: https://gitscripts.com/setup-git-ssh

## Rules for this repository
Even if chaos is expected for this repository, there must be some rules imposed to 
retain a good and proper workflow in order to practice a good process.

The rules are as follows:
1. `git_personal` are where private codes are stored. Codes stored within a specific
user's directory (i.e. `git_personal/username`) should only be modified by the
user assigned to it.
2. Codes within `git_personal` should be turned into a package that can be imported
by other directories.
3. All users can modify and delete all codes and add more codes inside `git_common`.
4. Create a `README.md` for created directories and packages.
5. Never delete root directories (i.e. `git_common`, `git_personal`).
6. Set appropriate tags for your code (i.e. `wip`).
7. Never steal the codes for your own personal gain and usage. Use it to learn and
experiment.
8. Always create a branch and never commit and push from master!
9. Branch names should be all lower case, no spaces, words are separated by hyphens.
If it is associated to a ticket (i.e. JIRA) then the ticket number must be the
prefix of the branch name.
i.e. `TIX-001/feature-branch-name`
10. Commit messages should be clean and easy to understand. Document all relevant changes.
11. Commit messages should start with:
    - Add
    - Update
    - Fix
    - Delete