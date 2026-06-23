def handler(store, request: dict) -> dict:
    return store.list_virtual_routers(request["meshName"], request.get("limit"), request.get("nextToken"), request.get("meshOwner"))
