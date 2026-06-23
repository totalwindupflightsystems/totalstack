def handler(store, request: dict) -> dict:
    record = store.delete_route(request["meshName"], request["virtualRouterName"], request["routeName"], request.get("meshOwner"))
    return record.to_dict()
