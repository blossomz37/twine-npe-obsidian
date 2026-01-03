---
description: Get a word count summary for manuscript files
---

# Word Count Workflow

Get word counts for your manuscript or individual chapters.

## When to Use

- Checking progress on your writing
- Verifying chapter lengths
- Tracking daily/weekly word count

## Steps

1. **Ask what to count**
   - Specific file(s)?
   - All chapters in a folder?
   - Entire manuscript?

2. **Count the words**
   
   For a single file:
   ```bash
   wc -w [filename]
   ```
   
   For all markdown files in a folder:
   ```bash
   wc -w chapters/*.md
   ```
   
   For all text/markdown files recursively:
   ```bash
   find . -name "*.md" -exec wc -w {} + | tail -1
   ```

3. **Present results clearly**
   
   Format as a table:
   | File | Words |
   |------|-------|
   | chapter-01.md | 3,245 |
   | chapter-02.md | 4,102 |
   | ... | ... |
   | **Total** | **XX,XXX** |

4. **Offer context** (optional)
   - Average chapter length
   - Comparison to previous count (if known)
   - Estimated reading time (words ÷ 250 = minutes)

## Example Output

```
📊 Word Count Report

| Chapter | Words |
|---------|-------|
| Chapter 1 - The Beginning | 3,245 |
| Chapter 2 - Rising Action | 4,102 |
| Chapter 3 - The Twist | 2,891 |

Total: 10,238 words
Average per chapter: 3,413 words
Estimated reading time: ~41 minutes
```
