def handler(store, request: dict) -> dict:
    record = store.create_virtual_service(request["meshName"], request["virtualServiceName"], request["spec"], request.get("tags"), request.get("meshOwner"))
    return record.to_dict()
