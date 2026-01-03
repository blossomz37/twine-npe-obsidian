# 🚀 Project Starter Kit

A ready-to-use template for AI-powered projects. Whether you're building with ChatGPT, Claude, or other AI tools, this kit gives you a solid foundation with best practices already set up.

---

## For AI Assistants

> **If you're an AI reading this:** This starter kit contains templates and working code for AI/LLM projects. Read each section below to understand what's included, then help your user decide which pieces they need based on their project goals. Create a customized task list for setting up their project.

---

## What's In This Kit?

This kit contains everything you need to start an AI-powered project. Here's what each file does:

### 📋 Template Files (Rename These)

| File | What It Does | Rename To |
|------|--------------|-----------|
| `sample.env.md` | Stores your secret API keys and settings | `.env` |
| `sample.gitignore.md` | Tells git which files to ignore | `.gitignore` |
| `sample.README.md` | A detailed project readme template | `README.md` |
| `sample.README_SIMPLE.md` | A simpler readme for non-technical projects | `README.md` |
| `sample.main.py` | A placeholder starting point for your code | `main.py` |
| `sample.requirements.txt` | List of Python packages you'll need | `requirements.txt` |
| `sample.LICENSE` | MIT license (lets others use your code) | `LICENSE` |

### 📁 Working Code (Ready to Use)

| Folder/File | What It Does |
|-------------|--------------|
| `config/settings.py` | Automatically loads your API keys and settings from `.env` |
| `src/utils.py` | Helper functions for caching API responses and saving output |

### 📂 Project Folders

| Folder | What It's For |
|--------|---------------|
| `.cache/` | Stores cached API responses (saves money!) |
| `output/` | Where generated content gets saved |

### 📖 Reference Guides

| File | What It Contains |
|------|------------------|
| `VIBECODE_PROJECT_STARTER.md` | Detailed guide on project structure, with code examples |

---

## Who Is This For?

### ✅ Great For:
- **Writers** using AI to help with creative projects
- **Content creators** generating text or images
- **Hobbyists** experimenting with AI APIs
- **Developers** who want a quick-start template
- **Anyone** working with ChatGPT, Claude, Gemini, or other AI tools

### ❓ You'll Need:
- A computer (Mac, Windows, or Linux)
- Python installed (version 3.10 or newer recommended)
- API keys from at least one AI provider (OpenAI, Anthropic, etc.)

### 🤔 Not Sure About Something?
Ask your AI assistant! They can explain any concept, walk you through setup, or help you decide what you need.

---

## Quick Decision Guide

Not sure what you need? Here's a simple guide:

### "I just want to run some AI scripts"
**Keep:**
- `sample.env.md` → `.env` (required for API keys)
- `sample.gitignore.md` → `.gitignore` (protects your secrets)
- `sample.main.py` → `main.py` (your starting point)
- `sample.requirements.txt` → `requirements.txt` (installs packages)

**Optional:**
- `config/` and `src/` folders (nice to have, but not required for simple scripts)

---

### "I want a well-organized project"
**Keep everything!** The full structure gives you:
- Proper settings management (`config/settings.py`)
- Caching to save money on API calls (`src/utils.py`)
- Clean separation of code and configuration
- Professional project structure

---

### "I'm sharing this with others"
**Also add:**
- `sample.README.md` or `sample.README_SIMPLE.md` → `README.md`
- `sample.LICENSE` → `LICENSE`

---

## Setup Steps

### Step 1: Rename the Folder
Change `Project_Starter_Kit_2025_01_03` to your project name (e.g., `my-story-generator`)

### Step 2: Rename Template Files
```bash
# Required
mv sample.env.md .env
mv sample.gitignore.md .gitignore
mv sample.main.py main.py
mv sample.requirements.txt requirements.txt

# Optional (choose one readme style)
mv sample.README.md README.md
# OR
mv sample.README_SIMPLE.md README.md

# Optional (if sharing publicly)
mv sample.LICENSE LICENSE
```

### Step 3: Add Your API Keys
1. Open `.env` in any text editor
2. Find the lines for your API provider(s)
3. Paste your key after the `=` sign
4. Save the file

### Step 4: Install Python Packages
```bash
pip install -r requirements.txt
```

### Step 5: Start Building!
```bash
python main.py
```

---

## File-by-File Details

### `sample.env.md` → `.env`
**What:** Your secret settings file  
**Contains:**
- API keys for OpenAI, Anthropic, Google, Mistral, OpenRouter
- Default model settings (which AI to use)
- Generation parameters (temperature, max tokens, etc.)
- Rate limiting (to avoid hitting API limits)
- Project directories (where to save files)

**Important:** Never share this file! It contains your secret keys.

---

### `sample.gitignore.md` → `.gitignore`
**What:** Tells git which files to ignore  
**Protects:**
- Your `.env` file (secret keys)
- System files (Mac's `.DS_Store`, Windows' `Thumbs.db`)
- Generated output and cache
- IDE settings

---

### `sample.README.md` (Developer Version)
**What:** Professional readme template  
**Includes:**
- Project description
- Installation steps
- Usage examples
- API documentation
- Contributing guidelines
- Troubleshooting

---

### `sample.README_SIMPLE.md` (Non-Coder Version)
**What:** Simplified readme for non-technical projects  
**Includes:**
- What it does (plain language)
- How to set it up
- How to use it
- Common problems and fixes

---

### `config/settings.py`
**What:** Automatically loads your `.env` settings into Python  
**Features:**
- Loads all API keys
- Sets default values if not specified
- Converts types (strings to numbers, etc.)
- Creates output directories automatically
- Validates that you have API keys configured

**Usage in your code:**
```python
from config.settings import OPENAI_API_KEY, DEFAULT_TEMP
```

---

### `src/utils.py`
**What:** Helper functions you'll use often  
**Features:**
- `save_to_cache()` / `load_from_cache()` — Save API responses to avoid paying twice
- `save_output()` — Save generated text to files
- `save_image()` — Save generated images
- `clear_cache()` — Delete all cached responses

**Usage in your code:**
```python
from src.utils import save_to_cache, load_from_cache, save_output
```

---

### `VIBECODE_PROJECT_STARTER.md`
**What:** Complete reference guide  
**Contains:**
- Full project structure diagrams
- Complete code for settings.py and utils.py
- Setup checklist
- Tips for working with AI

**Best for:** Reading when you want to understand how everything fits together

---

## Cleanup (After Setup)

Once you've renamed what you need, delete the extras:

```bash
# Delete unused sample files
rm sample.*.md sample.*.py sample.*.txt sample.LICENSE 2>/dev/null

# Keep or delete the guide (your choice)
rm VIBECODE_PROJECT_STARTER.md

# Delete this readme (replace with your own)
rm README.md
```

---

## Getting Help

**Not sure what to do next?** Ask your AI assistant:
- "Read the README and tell me what I need for [my project type]"
- "Help me set up this starter kit step by step"
- "Create a task list for getting my project started"
- "Explain what [any file] does"

---

## License

MIT — Use however you want, no restrictions.

---

Made with ❤️ for humans and AIs working together
