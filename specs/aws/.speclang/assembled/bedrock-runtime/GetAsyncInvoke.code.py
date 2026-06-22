def handler(store, request: dict) -> dict:
    """Get an async invoke job by ARN."""
    return store.get_async_invoke(request["invocationArn"])

