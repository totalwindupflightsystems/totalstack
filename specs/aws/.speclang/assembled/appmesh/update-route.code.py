def handler(store, request: dict) -> dict:
    record = store.update_route(request["meshName"], request["virtualRouterName"], request["routeName"], request["spec"], request.get("meshOwner"))
    return record.to_dict()
