def handler(store, request: dict) -> dict:
    return store.list_speech_synthesis_tasks(
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
        Status=request.get("Status"))

