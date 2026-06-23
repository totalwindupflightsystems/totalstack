def handler(store, request: dict) -> dict:
    return store.list_routes(request["meshName"], request["virtualRouterName"], request.get("limit"), request.get("nextToken"), request.get("meshOwner"))
