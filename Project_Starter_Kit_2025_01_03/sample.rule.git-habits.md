# Git Commit Habits

When working on tasks, follow these git practices to keep a clean history:

## After Completing Tasks

1. **Always commit after finishing a task** — Don't leave work uncommitted
2. **Group related changes together** — One commit per logical unit of work
3. **Keep unrelated changes separate** — Different tasks = different commits

## Commit Grouping Examples

### ✅ Good: Separate commits for separate work
```
Commit 1: "Add word count script and tests"
  - wordcount.py
  - test_wordcount.py

Commit 2: "Revise Chapter 3 dialogue"
  - chapters/chapter-03.md

Commit 3: "Fix typos in Chapter 1-2"
  - chapters/chapter-01.md
  - chapters/chapter-02.md
```

### ❌ Bad: Everything in one commit
```
Commit 1: "Various updates"
  - wordcount.py
  - test_wordcount.py
  - chapters/chapter-01.md
  - chapters/chapter-02.md
  - chapters/chapter-03.md
```

## Commit Message Format

Use clear, descriptive messages:
- `Add [feature]` — New functionality
- `Fix [issue]` — Bug fixes
- `Update [file]` — Changes to existing content
- `Revise [chapter/section]` — Editorial changes
- `Refactor [component]` — Code reorganization

## When to Commit

- ✅ After completing a task from the task list
- ✅ Before starting a completely different type of work
- ✅ When you have working code you don't want to lose
- ✅ Before experimenting with risky changes
