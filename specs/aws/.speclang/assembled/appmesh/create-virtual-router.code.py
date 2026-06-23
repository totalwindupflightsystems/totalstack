def handler(store, request: dict) -> dict:
    record = store.create_virtual_router(request["meshName"], request["virtualRouterName"], request["spec"], request.get("tags"), request.get("meshOwner"))
    return record.to_dict()
