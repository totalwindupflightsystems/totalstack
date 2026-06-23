def handler(store, request: dict) -> dict:
    return store.list_meshes(request.get("limit"), request.get("nextToken"))
