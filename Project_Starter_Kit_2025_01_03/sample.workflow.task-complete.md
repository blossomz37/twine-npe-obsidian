---
description: Complete a task and commit the changes with a clear message
---

# Task Complete Workflow

Use this after finishing any task to commit your work properly.

## Steps

1. **Summarize what was done**
   - List the files that were created or modified
   - Briefly describe what changed

2. **Check for uncommitted work**
   ```bash
   git status
   ```

3. **Stage the relevant files**
   - Only stage files related to THIS task
   - If unrelated files are modified, leave them for a separate commit
   ```bash
   git add [files related to this task]
   ```

4. **Commit with a clear message**
   ```bash
   git commit -m "[type]: [what was accomplished]"
   ```
   
   Use these prefixes:
   - `Add:` — Created something new
   - `Update:` — Modified existing files
   - `Fix:` — Corrected an issue
   - `Revise:` — Editorial changes to content
   - `Delete:` — Removed files or content

5. **Confirm the commit**
   ```bash
   git log -1 --oneline
   ```

6. **Report to user**
   - Show what was committed
   - Mention any remaining uncommitted files (for other tasks)

## Example Output

```
✅ Task Complete: Created word count script

Committed:
- wordcount.py (new)
- test_wordcount.py (new)

Commit: a1b2c3d "Add: word count script with tests"

Note: chapter-05.md has changes from a different task (not committed)
```
