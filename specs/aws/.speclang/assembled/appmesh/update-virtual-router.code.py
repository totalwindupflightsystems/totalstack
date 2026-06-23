def handler(store, request: dict) -> dict:
    record = store.update_virtual_router(request["meshName"], request["virtualRouterName"], request["spec"], request.get("meshOwner"))
    return record.to_dict()
