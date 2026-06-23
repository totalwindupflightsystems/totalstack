def handler(store, request: dict) -> dict:
    record = store.update_virtual_service(request["meshName"], request["virtualServiceName"], request["spec"], request.get("meshOwner"))
    return record.to_dict()
