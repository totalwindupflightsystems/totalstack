def handler(store, request: dict) -> dict:
    record = store.describe_virtual_service(request["meshName"], request["virtualServiceName"], request.get("meshOwner"))
    return record.to_dict()
