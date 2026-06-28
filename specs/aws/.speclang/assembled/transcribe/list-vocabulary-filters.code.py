def handler(store, request: dict) -> dict:
    return store.list_vocabulary_filters(
        NextToken=request.get("NextToken"),
        MaxResults=request.get("MaxResults"),
        NameContains=request.get("NameContains"))

