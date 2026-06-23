def handler(store, request: dict) -> dict:
    record = store.create_route(request["meshName"], request["virtualRouterName"], request["routeName"], request["spec"], request.get("tags"), request.get("meshOwner"))
    return record.to_dict()
