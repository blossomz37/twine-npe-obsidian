---
description: List available workflows and explain what they do
---

# Help - What Can You Do?

Show the user what workflows are available in this project.

## Steps

1. **List all workflow files** in `.agent/workflows/`
   ```bash
   ls -1 .agent/workflows/
   ```

2. **For each workflow**, read the description from the YAML frontmatter

3. **Present a helpful summary**:

   ```
   📋 Available Workflows

   Type these in chat to trigger them:

   /smart-commit     - Commit work with grouped, organized changes
   /task-complete    - Finish a task and commit the results
   /word-count       - Get word counts for your manuscript
   /help             - Show this list (you're here!)

   💡 Tip: You can also just describe what you want in plain English!
   ```

4. **Offer to explain any workflow** in more detail if asked
