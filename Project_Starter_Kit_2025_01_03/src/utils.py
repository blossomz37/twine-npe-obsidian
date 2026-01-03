"""
Utility Functions
==================
Common helpers for caching, file output, and other tasks.

Usage:
    from src.utils import load_from_cache, save_to_cache, save_output
"""

import os
import json
import hashlib
from config.settings import CACHE_DIR, OUTPUT_DIR


# ===================
# Caching
# ===================

def get_cache_path(key: str) -> str:
    """
    Generate a cache file path from a key.
    
    Args:
        key: A unique string identifier (e.g., prompt + model name)
    
    Returns:
        Path to the cache file
    """
    hash_key = hashlib.md5(key.encode()).hexdigest()
    return os.path.join(CACHE_DIR, f"{hash_key}.json")


def load_from_cache(key: str):
    """
    Load a cached response if it exists.
    
    Args:
        key: The same key used when saving
    
    Returns:
        Cached data, or None if not found
    """
    path = get_cache_path(key)
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return None


def save_to_cache(key: str, data):
    """
    Save a response to cache.
    
    Args:
        key: A unique string identifier
        data: JSON-serializable data to cache
    """
    path = get_cache_path(key)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def clear_cache():
    """Remove all cached files."""
    import shutil
    if os.path.exists(CACHE_DIR):
        shutil.rmtree(CACHE_DIR)
        os.makedirs(CACHE_DIR, exist_ok=True)
        print(f"🗑️  Cleared cache: {CACHE_DIR}")


# ===================
# Output Saving
# ===================

def save_output(content: str, filename: str, subdir: str = "text") -> str:
    """
    Save generated content to the output directory.
    
    Args:
        content: The content to save
        filename: Name of the file (e.g., "story.txt")
        subdir: Subdirectory within output/ (default: "text")
    
    Returns:
        Full path to the saved file
    """
    path = os.path.join(OUTPUT_DIR, subdir, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"💾 Saved: {path}")
    return path


def save_image(image_data: bytes, filename: str) -> str:
    """
    Save image data to the output/images directory.
    
    Args:
        image_data: Raw image bytes
        filename: Name of the file (e.g., "generated.png")
    
    Returns:
        Full path to the saved file
    """
    path = os.path.join(OUTPUT_DIR, "images", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        f.write(image_data)
    print(f"🖼️  Saved: {path}")
    return path


# ===================
# Helpers
# ===================

def make_cache_key(*args) -> str:
    """
    Create a cache key from multiple arguments.
    
    Example:
        key = make_cache_key(prompt, model, temperature)
    """
    return "|".join(str(arg) for arg in args)


if __name__ == "__main__":
    # Quick test when running directly
    print("Testing cache...")
    save_to_cache("test_key", {"message": "Hello, cache!"})
    result = load_from_cache("test_key")
    print(f"Loaded from cache: {result}")
    
    print("\nTesting output...")
    save_output("Hello, world!", "test.txt")
