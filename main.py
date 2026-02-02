"""
News analysis system with multiple API's.
"""

API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "en"


def clean_text(text: str) -> str:
    """Cleans and normalizes text."""
    if not text:
        return ""
    return text.strip().lower()


def validate_api_key(api_key: str) -> bool:
    """Validates API key has correct format."""
    return len(api_key) > 10 and api_key.isalnum()
