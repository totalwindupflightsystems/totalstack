def handler(store, request: dict) -> dict:
    return store.list_virtual_nodes(request["meshName"], request.get("limit"), request.get("nextToken"), request.get("meshOwner"))
