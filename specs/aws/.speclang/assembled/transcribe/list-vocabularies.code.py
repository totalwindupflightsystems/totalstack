def handler(store, request: dict) -> dict:
    return store.list_vocabularies(
        NextToken=request.get("NextToken"),
        MaxResults=request.get("MaxResults"),
        StateEquals=request.get("StateEquals"),
        NameContains=request.get("NameContains"))

