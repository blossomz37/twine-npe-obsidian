# Markdown to DOCX Converter

A simple script to convert Markdown files to Word documents.

## Requirements

- Python 3.10+
- Pandoc installed on your system

### Install Pandoc

**Mac:**
```bash
brew install pandoc
```

**Windows:**
Download from https://pandoc.org/installing.html

**Linux:**
```bash
sudo apt install pandoc
```

### Install Python Package

```bash
pip install pypandoc
```

## Usage

### Single File

1. Edit `convert.py` and set your input/output files
2. Run: `python convert.py`

### Batch Conversion

1. Put your `.md` files in the `input/` folder
2. Run: `python convert_batch.py`
3. Find your `.docx` files in the `output/` folder

## Files

| File | Purpose |
|------|---------|
| `convert.py` | Convert a single markdown file |
| `convert_batch.py` | Convert all markdown files in a folder |
| `input/` | Put your markdown files here (for batch) |
| `output/` | Converted files appear here |
| `sample.md` | Example markdown file to test |
