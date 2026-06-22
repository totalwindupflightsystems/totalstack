def handler(store, request: dict) -> dict:
    return store.list_provisioned_model_throughputs(
        creationTimeAfter=request.get("creationTimeAfter"),
        creationTimeBefore=request.get("creationTimeBefore"),
        statusEquals=request.get("statusEquals"),
        modelArnEquals=request.get("modelArnEquals"),
        nameContains=request.get("nameContains"),
        maxResults=request.get("maxResults"),
        nextToken=request.get("nextToken"),
        sortBy=request.get("sortBy"),
        sortOrder=request.get("sortOrder"))
