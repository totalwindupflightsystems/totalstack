def handler(store, request: dict) -> dict:
    record = store.describe_virtual_router(request["meshName"], request["virtualRouterName"], request.get("meshOwner"))
    return record.to_dict()
