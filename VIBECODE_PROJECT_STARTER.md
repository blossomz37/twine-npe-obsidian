# Vibecode Project Starter Guide

A recommended project structure for AI/LLM projects using the configuration in `sample.env.md`.

---

## Quick Start (Minimal Structure)

For rapid prototyping and vibecoding:

```
my-project/
├── .env                 # Your secrets (copy from sample.env)
├── .gitignore           # Copy from sample.gitignore.md
├── main.py              # Everything in one file
├── requirements.txt     # Dependencies
├── .cache/              # Cached API responses (gitignored)
└── output/              # Generated content (gitignored)
```

---

## Full Project Structure

For more organized, scalable projects:

```
my-ai-project/
├── .env                      # Your actual secrets (from sample.env)
├── .gitignore                # Ignore .env, cache, output, etc.
├── README.md                 # Project overview & setup instructions
├── requirements.txt          # Python dependencies
│
├── config/
│   ├── __init__.py
│   ├── settings.py           # Load & validate .env variables
│   └── models.py             # Model configurations & defaults
│
├── src/
│   ├── __init__.py
│   ├── client.py             # API client with rate limiting
│   ├── text_gen.py           # Text generation functions
│   ├── image_gen.py          # Image generation (OpenRouter, etc.)
│   └── utils.py              # Helpers (retry logic, response parsing)
│
├── templates/                # Reusable prompt templates (optional)
│   ├── summarize.txt
│   └── analyze.txt
│
├── scripts/                  # Entry points / CLI scripts
│   ├── generate.py           # Main generation script
│   └── batch_process.py      # Batch processing with rate limits
│
├── .cache/                   # Cached API responses (gitignored)
│   └── responses/
│
├── output/                   # Generated content (gitignored)
│   ├── text/
│   └── images/
│
└── tests/                    # Unit tests
    ├── test_client.py
    └── test_generators.py
```

---

## Key Files

### `config/settings.py`

Central place to load and validate your `.env`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

# ===================
# API Keys
# ===================
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# ===================
# Models
# ===================
DEFAULT_TEXT_MODEL = os.getenv("DEFAULT_TEXT_MODEL", "gpt-4o")
DEFAULT_IMAGE_MODEL = os.getenv("DEFAULT_IMAGE_MODEL", "dall-e-3")

# ===================
# Text Generation Parameters
# ===================
DEFAULT_TEMP = float(os.getenv("DEFAULT_TEMP", 0.7))
DEFAULT_MAX_TOKENS = int(os.getenv("DEFAULT_MAX_TOKENS", 4096))
DEFAULT_TOP_P = float(os.getenv("DEFAULT_TOP_P", 1.0))
DEFAULT_FREQUENCY_PENALTY = float(os.getenv("DEFAULT_FREQUENCY_PENALTY", 0))
DEFAULT_PRESENCE_PENALTY = float(os.getenv("DEFAULT_PRESENCE_PENALTY", 0))
DEFAULT_STREAM = os.getenv("DEFAULT_STREAM", "true").lower() == "true"

# ===================
# Rate Limiting
# ===================
RATE_LIMIT_RPM = int(os.getenv("RATE_LIMIT_RPM", 60))
RATE_LIMIT_TPM = int(os.getenv("RATE_LIMIT_TPM", 100000))

# ===================
# System Settings
# ===================
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 60))
DEFAULT_RETRY_COUNT = int(os.getenv("DEFAULT_RETRY_COUNT", 3))
DEFAULT_FALLBACK_MODEL = os.getenv("DEFAULT_FALLBACK_MODEL", "")

# ===================
# Directories
# ===================
CACHE_DIR = os.getenv("CACHE_DIR", ".cache")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")

# Ensure directories exist
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "text"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "images"), exist_ok=True)
```

---

### `src/client.py`

API client with built-in rate limiting:

```python
import time
from config.settings import RATE_LIMIT_RPM, DEFAULT_RETRY_COUNT, DEFAULT_TIMEOUT

class RateLimitedClient:
    """API client that respects rate limits."""
    
    def __init__(self, rpm=None):
        self.rpm = rpm or RATE_LIMIT_RPM
        self.min_delay = 60 / self.rpm
        self.last_request = 0
    
    def _throttle(self):
        """Wait if we're making requests too quickly."""
        elapsed = time.time() - self.last_request
        if elapsed < self.min_delay:
            time.sleep(self.min_delay - elapsed)
        self.last_request = time.time()
    
    def call(self, func, *args, **kwargs):
        """Execute a function with rate limiting."""
        self._throttle()
        return func(*args, **kwargs)
    
    def call_with_retry(self, func, *args, retries=None, **kwargs):
        """Execute with rate limiting and automatic retry on failure."""
        retries = retries or DEFAULT_RETRY_COUNT
        last_error = None
        
        for attempt in range(retries):
            try:
                return self.call(func, *args, **kwargs)
            except Exception as e:
                last_error = e
                wait_time = (2 ** attempt)  # Exponential backoff
                print(f"Attempt {attempt + 1} failed, retrying in {wait_time}s...")
                time.sleep(wait_time)
        
        raise last_error
```

---

### `src/utils.py`

Common utility functions:

```python
import os
import json
import hashlib
from config.settings import CACHE_DIR

def get_cache_path(key: str) -> str:
    """Generate a cache file path from a key."""
    hash_key = hashlib.md5(key.encode()).hexdigest()
    return os.path.join(CACHE_DIR, f"{hash_key}.json")

def load_from_cache(key: str):
    """Load a cached response if it exists."""
    path = get_cache_path(key)
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return None

def save_to_cache(key: str, data):
    """Save a response to cache."""
    path = get_cache_path(key)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f)

def save_output(content: str, filename: str, subdir: str = "text"):
    """Save generated content to the output directory."""
    from config.settings import OUTPUT_DIR
    path = os.path.join(OUTPUT_DIR, subdir, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    return path
```

---

## `requirements.txt`

Minimal dependencies to get started:

```
python-dotenv>=1.0.0
openai>=1.0.0
anthropic>=0.20.0
requests>=2.31.0
```

---

## Setup Checklist

1. [ ] Copy `sample.env` → `.env` and fill in your API keys
2. [ ] Copy `sample.gitignore.md` → `.gitignore`
3. [ ] Create `requirements.txt` with your dependencies
4. [ ] Run `pip install -r requirements.txt`
5. [ ] Create your project structure (minimal or full)
6. [ ] Start vibecoding! 🚀

---

## Tips for Vibecoding

1. **Start minimal** — Use the quick start structure, expand later
2. **Cache everything** — API calls cost money; cache responses during development
3. **Use rate limits** — Better slow than blocked
4. **Git commit often** — Before major experiments, commit your working state
5. **Keep `.env` safe** — Never commit secrets, always use `.gitignore`

---

## Related Files

- [`sample.env.md`](./sample.env.md) — Environment variable template
- [`sample.gitignore.md`](./sample.gitignore.md) — Gitignore template
- [`.gitignore`](./.gitignore) — Active gitignore for this project
