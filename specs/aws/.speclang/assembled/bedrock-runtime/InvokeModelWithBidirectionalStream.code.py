def handler(store, request: dict) -> dict:
    """Invoke a foundation model with bidirectional streaming."""
    return {
        "body": "{\"bidirectional_response\": \"mock\"}",
    }

