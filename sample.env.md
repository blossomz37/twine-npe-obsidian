# ============================================
# Sample Environment Configuration File
# ============================================
# 
# SETUP INSTRUCTIONS:
# 1. Rename this file from 'sample.env.md' to '.env'
# 2. Save it to the root of your project directory
# 3. Fill in your API keys and configuration values
# 4. NEVER commit `.env`this file to version control! Make sure it is added to your .gitignore file.
#
# NOTE: This is a starter template. Add or remove
# variables based on your project's requirements.
# ============================================


# ============================================
# API Keys
# ============================================
# Get your API keys from the respective providers:
# - OpenRouter: https://openrouter.ai/keys
# - OpenAI: https://platform.openai.com/api-keys
# - Mistral: https://console.mistral.ai/api-keys
# - Google: https://aistudio.google.com/apikey
# - Anthropic: https://console.anthropic.com/settings/keys

OPENROUTER_API_KEY=
OPENAI_API_KEY=
MISTRAL_API_KEY=
GOOGLE_API_KEY=
ANTHROPIC_API_KEY=


# ============================================
# Default Model Settings
# ============================================
# Specify the default models for image and text generation.
# Examples:
#   Image: dall-e-3, stable-diffusion-xl, midjourney
#   Text: gpt-4o, claude-3-opus, gemini-pro, mistral-large

DEFAULT_IMAGE_MODEL=
DEFAULT_TEXT_MODEL=


# ============================================
# Generation Parameters
# ============================================
# TEMP: Controls randomness (0.0 = deterministic, 1.0+ = creative)
# MAX_TOKENS: Maximum length of generated responses
# REASONING: Enable extended thinking/reasoning (true/false)

DEFAULT_TEMP=0.7
DEFAULT_MAX_TOKENS=4096
DEFAULT_REASONING=false


# ============================================
# Optional: Additional Configuration
# ============================================
# Add any project-specific variables below

# DATABASE_URL=
# REDIS_URL=
# LOG_LEVEL=info
# DEBUG=false
