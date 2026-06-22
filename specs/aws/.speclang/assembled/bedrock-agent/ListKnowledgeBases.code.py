def handler(store, request: dict) -> dict:
    return store.list_knowledge_bases(
        maxResults=request.get("maxResults"),
        nextToken=request.get("nextToken"))
