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
FALLBACK_IMAGE_MODEL=
DEFAULT_TEXT_MODEL=
FALLBACK_TEXT_MODEL=


# ============================================
# Text Generation Parameters
# ============================================
# TEMP: Controls randomness (0.0 = deterministic, 1.0+ = creative)
# MAX_TOKENS: Maximum length of generated responses
# REASONING: Enable extended thinking/reasoning (true/false)
# TOP_P: Nucleus sampling threshold (0.0-1.0), alternative to temperature
# TOP_K: Limits token selection to top K most likely options
# FREQUENCY_PENALTY: Reduces repetition of tokens (-2.0 to 2.0)
# PRESENCE_PENALTY: Encourages introducing new topics (-2.0 to 2.0)
# STOP_SEQUENCES: Comma-separated strings that stop generation
# STREAM: Enable streaming responses (true/false)
# SEED: For reproducible outputs (integer, optional)

DEFAULT_TEMP=0.7
DEFAULT_MAX_TOKENS=4096
DEFAULT_REASONING=false
DEFAULT_TOP_P=1.0
DEFAULT_TOP_K=
DEFAULT_FREQUENCY_PENALTY=0
DEFAULT_PRESENCE_PENALTY=0
DEFAULT_STOP_SEQUENCES=
DEFAULT_STREAM=true
DEFAULT_SEED=


# ============================================
# Image Generation Parameters
# ============================================
# IMAGE_SIZE: Output dimensions (e.g., 1024x1024, 1792x1024, 16:9)
# IMAGE_QUALITY: Quality level (standard, hd)
# IMAGE_STYLE: Style preset (natural, vivid, cinematic)
# IMAGE_COUNT: Number of images per request

DEFAULT_IMAGE_SIZE=1024x1024
DEFAULT_IMAGE_QUALITY=standard
DEFAULT_IMAGE_STYLE=natural
DEFAULT_IMAGE_COUNT=1


# ============================================
# OpenRouter Image Generation Settings
# ============================================
# Required: Set modalities to enable image output
# MODALITIES: Must include "image" for image generation (JSON array format)
#   Options: ["text"], ["image", "text"]
#
# IMAGE_CONFIG options (Gemini models):
# ASPECT_RATIO: Image aspect ratio
#   Supported: 1:1 (default), 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9
#   Dimensions: 1:1=1024x1024, 16:9=1344x768, 9:16=768x1344, etc.
# IMAGE_RESOLUTION: Resolution tier (Gemini only)
#   Options: 1K (default), 2K, 4K
#
# Compatible Models (check output_modalities includes "image"):
#   - google/gemini-2.5-flash-image-preview
#   - black-forest-labs/flux.2-pro
#   - black-forest-labs/flux.2-flex
#   - sourceful/riverflow-v2-standard-preview

OPENROUTER_MODALITIES=["image", "text"]
OPENROUTER_ASPECT_RATIO=16:9
OPENROUTER_IMAGE_RESOLUTION=1K
OPENROUTER_DEFAULT_IMAGE_MODEL=google/gemini-2.5-flash-image-preview


# ============================================
# System & Retry Settings
# ============================================
# TIMEOUT: Request timeout in seconds
# RETRY_COUNT: Number of retry attempts on failure
# FALLBACK_MODEL: Backup model if primary fails

DEFAULT_TIMEOUT=60
DEFAULT_RETRY_COUNT=3
DEFAULT_FALLBACK_MODEL=


# ============================================
# Rate Limiting
# ============================================
# Self-throttle to avoid hitting API limits and getting 429 errors
# RPM: Requests Per Minute (how many API calls per minute)
# TPM: Tokens Per Minute (total tokens sent + received per minute)
# Check your provider's limits: OpenAI, Anthropic, etc. vary by tier

RATE_LIMIT_RPM=60
RATE_LIMIT_TPM=100000


# ============================================
# Project Directories
# ============================================
# CACHE_DIR: Store cached API responses to avoid redundant calls
# OUTPUT_DIR: Where generated content (text, images, etc.) is saved
# TIP: Add these directories to your .gitignore if they contain generated content

CACHE_DIR=.cache
OUTPUT_DIR=output


# ============================================
# Optional: Additional Configuration
# ============================================
# Add any project-specific variables below

PROJECT_NAME=
ENVIRONMENT=development
LOG_LEVEL=info
DEBUG=false

# DATABASE_URL=
# REDIS_URL=
