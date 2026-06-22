def handler(store, request: dict) -> dict:
    """Invoke a foundation model (legacy API)."""
    return {
        "body": "{\"completion\": \"This is a mock model response.\"}",
        "contentType": "application/json",
    }

