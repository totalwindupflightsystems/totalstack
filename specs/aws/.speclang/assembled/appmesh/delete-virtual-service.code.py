def handler(store, request: dict) -> dict:
    record = store.delete_virtual_service(request["meshName"], request["virtualServiceName"], request.get("meshOwner"))
    return record.to_dict()
