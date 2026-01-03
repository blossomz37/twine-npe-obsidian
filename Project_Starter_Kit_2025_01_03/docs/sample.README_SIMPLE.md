# Simple README Template

> **Setup Instructions:**
> 1. Rename this file from `sample.README-simple.md` to `README.md`
> 2. Replace all `[placeholder]` text with your project's information
> 3. Delete this instruction block when done

---

# [Project Name]

[One-line description of what your project does]

## What This Does

[2-3 sentences explaining what this project is. Write it like you're explaining to a friend who's never seen it before.]

---

## Quick Start

### First Time Setup

```bash
# 1. Open Terminal and go to your project folder
cd [project-name]

# 2. Set up your settings file
cp sample.env .env

# 3. Edit .env and add your API keys (see below)

# 4. Run the project
python main.py
```

### Running It Again Later

```bash
cd [project-name]
python main.py
```

---

## API Keys You'll Need

Before running, you need to get API keys and add them to your `.env` file:

| Key | Where to Get It | Required? |
|-----|-----------------|-----------|
| `OPENAI_API_KEY` | [OpenAI](https://platform.openai.com/api-keys) | Yes |
| `ANTHROPIC_API_KEY` | [Anthropic](https://console.anthropic.com/settings/keys) | Optional |

**How to add your keys:**
1. Open the `.env` file in any text editor
2. Find the line with the key name (e.g., `OPENAI_API_KEY=`)
3. Paste your key after the `=` sign
4. Save the file

---

## How to Use

[Explain in simple terms how someone uses this. For example:]

1. Run the script with `python main.py`
2. [What happens next]
3. [Where to find the output]

---

## Common Problems & Fixes

**"Command not found: python"**
- Try using `python3` instead of `python`

**"API key invalid" or "Authentication error"**
- Double-check your API key in `.env`
- Make sure there are no extra spaces
- Verify your key is still active on the provider's website

**"Rate limit exceeded"**
- Wait a few minutes and try again
- You may be making too many requests too quickly

**Something else not working?**
- [Contact info or where to get help]

---

## License

This project is licensed under the MIT License — do whatever you want with it, just don't blame me if something breaks.

---

## Need Help?

**[Your Name]**
- Email: your.email@example.com
- GitHub: [@username](https://github.com/username)
