def handler(store, request: dict) -> dict:
    return store.list_transcription_jobs(
        Status=request.get("Status"),
        JobNameContains=request.get("JobNameContains"),
        NextToken=request.get("NextToken"),
        MaxResults=request.get("MaxResults"))

