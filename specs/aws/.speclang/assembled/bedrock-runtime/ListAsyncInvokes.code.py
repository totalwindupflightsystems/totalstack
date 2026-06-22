def handler(store, request: dict) -> dict:
    """List async invoke jobs with optional filters."""
    return store.list_async_invokes(
        maxResults=request.get("maxResults"),
        statusEquals=request.get("statusEquals"),
        submitTimeAfter=request.get("submitTimeAfter"),
        submitTimeBefore=request.get("submitTimeBefore"),
        sortBy=request.get("sortBy"),
        sortOrder=request.get("sortOrder"),
        nextToken=request.get("nextToken"),
    )

