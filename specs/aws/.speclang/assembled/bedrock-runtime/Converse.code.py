def handler(store, request: dict) -> dict:
    """Converse with a foundation model."""
    return {
        "output": {"message": {"role": "assistant", "content": [{"text": "Hello! How can I help you?"}]}},
        "stopReason": "end_turn",
        "usage": {"inputTokens": 10, "outputTokens": 15, "totalTokens": 25},
        "metrics": {"latencyMs": 150},
    }

