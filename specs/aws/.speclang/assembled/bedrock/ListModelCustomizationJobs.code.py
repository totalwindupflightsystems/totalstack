def handler(store, request: dict) -> dict:
    return store.list_model_customization_jobs(
        creationTimeAfter=request.get("creationTimeAfter"),
        creationTimeBefore=request.get("creationTimeBefore"),
        statusEquals=request.get("statusEquals"),
        nameContains=request.get("nameContains"),
        maxResults=request.get("maxResults"),
        nextToken=request.get("nextToken"),
        sortBy=request.get("sortBy"),
        sortOrder=request.get("sortOrder"))
