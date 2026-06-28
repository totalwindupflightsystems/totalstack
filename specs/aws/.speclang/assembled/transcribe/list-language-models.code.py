def handler(store, request: dict) -> dict:
    return store.list_language_models(
        StatusEquals=request.get("StatusEquals"),
        NameContains=request.get("NameContains"),
        NextToken=request.get("NextToken"),
        MaxResults=request.get("MaxResults"))

