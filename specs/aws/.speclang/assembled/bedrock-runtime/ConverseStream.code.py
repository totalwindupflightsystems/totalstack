def handler(store, request: dict) -> dict:
    """Converse with a foundation model with streaming response."""
    return {
        "stream": [{"contentBlockDelta": {"contentBlockIndex": 0, "delta": {"text": "Hello! "}}},
                   {"contentBlockDelta": {"contentBlockIndex": 0, "delta": {"text": "How can I help?"}}},
                   {"contentBlockStop": {"contentBlockIndex": 0}},
                   {"messageStop": {"stopReason": "end_turn"}},
                   {"metadata": {"usage": {"inputTokens": 10, "outputTokens": 15, "totalTokens": 25}}}],
    }

