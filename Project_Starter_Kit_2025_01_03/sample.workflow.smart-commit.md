---
description: Commit completed work with a clear message, grouping related changes
---

# Smart Commit Workflow

This workflow helps you commit your work with good organization.

## Steps

1. **Review what's changed**
   - Run `git status` to see all modified files
   - List the changes and group them by purpose (e.g., "script changes", "chapter revisions", "config updates")

2. **For each group of related changes:**
   
   a. **Stage the related files**
      ```bash
      git add [file1] [file2] ...
      ```
   
   b. **Commit with a descriptive message**
      ```bash
      git commit -m "[type]: [brief description]"
      ```
      
      Message types:
      - `Add:` New files or features
      - `Update:` Changes to existing content
      - `Fix:` Bug fixes or corrections
      - `Revise:` Editorial/content changes
      - `Refactor:` Code reorganization

3. **Repeat for each group** until all changes are committed

4. **Confirm completion**
   - Run `git status` to verify working directory is clean
   - Run `git log -3` to show the last 3 commits

## Example

If the user completed:
- A word count script (wordcount.py)
- Tests for the script (test_wordcount.py)  
- Revised Chapter 5 (chapter-05.md)

Create TWO commits:
```bash
# Commit 1: Script work
git add wordcount.py test_wordcount.py
git commit -m "Add: word count script with tests"

# Commit 2: Writing work
git add chapter-05.md
git commit -m "Revise: Chapter 5 dialogue and pacing"
```
