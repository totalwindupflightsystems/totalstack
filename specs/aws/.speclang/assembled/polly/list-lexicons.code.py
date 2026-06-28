def handler(store, request: dict) -> dict:
    return store.list_lexicons(NextToken=request.get("NextToken"))

