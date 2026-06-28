def handler(store, request: dict) -> dict:
    return store.list_resource_types(
        nextToken=request.get("nextToken"),
        maxResults=request.get("maxResults"),
        resourceRegionScope=request.get("resourceRegionScope"),
    )
