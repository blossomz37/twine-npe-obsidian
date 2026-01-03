# 🚀 Project Starter Kit

A ready-to-use template for AI-powered projects. Whether you're building with ChatGPT, Claude, Gemini, or other AI tools, this kit gives you a solid foundation.

---

## For AI Assistants

> **If you're an AI reading this:** This starter kit contains templates and working code for AI/LLM projects. Read each section to understand what's included, then help your user decide which pieces they need and create a setup task list.

---

## What's Included

### 📋 Core Templates (at root)

| File | Rename To | Purpose |
|------|-----------|---------|
| `sample.env.md` | `.env` | API keys and settings |
| `sample.gitignore.md` | `.gitignore` | Files git should ignore |
| `sample.main.py` | `main.py` | Starting point for code |
| `sample.requirements.txt` | `requirements.txt` | Python packages |
| `sample.LICENSE` | `LICENSE` | MIT license |

### 📁 Working Code

| Folder | What It Does |
|--------|--------------|
| `config/settings.py` | Loads your `.env` variables into Python |
| `src/utils.py` | Helpers for caching and saving output |

### 📂 Project Folders

| Folder | Purpose |
|--------|---------|
| `.cache/` | Cached API responses |
| `output/` | Generated content |
| `.agent/` | Antigravity rules & workflows |

### 📖 Documentation (in `docs/`)

| File | What It Contains |
|------|------------------|
| `VIBECODE_PROJECT_STARTER.md` | Detailed project structure guide |
| `sample.README.md` | Full README template (for developers) |
| `sample.README_SIMPLE.md` | Simple README template (for non-coders) |

### 🤖 Antigravity Customizations (in `docs/antigravity/`)

| File | Type | What It Does |
|------|------|--------------|
| `sample.rule.git-habits.md` | Rule | Commit after tasks, group related changes |
| `sample.rule.communication-style.md` | Rule | Plain language, explain before doing |
| `sample.workflow.smart-commit.md` | Workflow | Organize commits by related changes |
| `sample.workflow.task-complete.md` | Workflow | Commit work after finishing a task |
| `sample.workflow.word-count.md` | Workflow | Count words in manuscript files |

---

## Quick Start

### 1. Rename the Folder
```
Project_Starter_Kit_2025_01_03  →  my-project-name
```

### 2. Rename Core Templates
```bash
cd my-project-name
mv sample.env.md .env
mv sample.gitignore.md .gitignore
mv sample.main.py main.py
mv sample.requirements.txt requirements.txt
mv sample.LICENSE LICENSE
```

### 3. Add Your API Keys
Open `.env` and add your keys from:
- [OpenAI](https://platform.openai.com/api-keys)
- [Anthropic](https://console.anthropic.com/settings/keys)
- [Google](https://aistudio.google.com/apikey)
- [OpenRouter](https://openrouter.ai/keys)

### 4. Install Packages
```bash
pip install -r requirements.txt
```

### 5. Start Building!
```bash
python main.py
```

---

## Optional: Copy a README Template

Choose one from `docs/`:
```bash
# For developers
cp docs/sample.README.md README.md

# For non-technical projects
cp docs/sample.README_SIMPLE.md README.md
```

---

## Optional: Set Up Antigravity

If using an AI assistant (like Antigravity), copy the rules and workflows:

```bash
# Copy rules
cp docs/antigravity/sample.rule.*.md .agent/rules/

# Copy workflows
cp docs/antigravity/sample.workflow.*.md .agent/workflows/

# Rename them (remove 'sample.' prefix)
cd .agent/rules && for f in sample.*.md; do mv "$f" "${f#sample.}"; done
cd ../workflows && for f in sample.*.md; do mv "$f" "${f#sample.}"; done
```

---

## Cleanup

After setup, delete what you don't need:
```bash
# Remove sample files
rm sample.* 2>/dev/null

# Remove docs if you don't need the reference
rm -rf docs/
```

---

## Getting Help

Ask your AI assistant:
- "Read the README and tell me what I need for my project"
- "Help me set up this starter kit step by step"
- "Create a task list for getting started"

---

## License

MIT — Use however you want.
