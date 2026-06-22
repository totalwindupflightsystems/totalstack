def handler(store, request: dict) -> dict:
    return store.list_data_sources(
        request["knowledgeBaseId"],
        maxResults=request.get("maxResults"),
        nextToken=request.get("nextToken"))
