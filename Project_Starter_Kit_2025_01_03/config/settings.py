"""
Settings Module
================
Loads and validates environment variables from .env file.

Usage:
    from config.settings import OPENAI_API_KEY, DEFAULT_TEMP
"""

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
DEFAULT_REASONING = os.getenv("DEFAULT_REASONING", "false").lower() == "true"

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
# Project Info
# ===================
PROJECT_NAME = os.getenv("PROJECT_NAME", "my-project")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

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


# ===================
# Validation (Optional)
# ===================
def validate_api_keys():
    """Check that at least one API key is configured."""
    keys = [OPENROUTER_API_KEY, OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_API_KEY, MISTRAL_API_KEY]
    if not any(keys):
        print("⚠️  Warning: No API keys configured. Add them to your .env file.")
        return False
    return True


if __name__ == "__main__":
    # Quick test when running directly
    print(f"Project: {PROJECT_NAME}")
    print(f"Environment: {ENVIRONMENT}")
    print(f"Debug: {DEBUG}")
    print(f"Cache Dir: {CACHE_DIR}")
    print(f"Output Dir: {OUTPUT_DIR}")
    validate_api_keys()
