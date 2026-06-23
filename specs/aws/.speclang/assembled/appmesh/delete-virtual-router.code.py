def handler(store, request: dict) -> dict:
    record = store.delete_virtual_router(request["meshName"], request["virtualRouterName"], request.get("meshOwner"))
    return record.to_dict()
