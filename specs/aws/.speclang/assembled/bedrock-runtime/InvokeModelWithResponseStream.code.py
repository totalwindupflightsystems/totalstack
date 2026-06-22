def handler(store, request: dict) -> dict:
    """Invoke a foundation model with streaming response (legacy)."""
    return {
        "body": "{\"chunk\": \"Hello world streaming\"}",
        "contentType": "application/json",
    }

