def handler(store, request: dict) -> dict:
    """Count tokens in input text."""
    input_data = request.get("input", {})
    text = input_data.get("text", "") if isinstance(input_data, dict) else str(input_data)
    return {"inputTokens": max(1, len(text) // 4)}

