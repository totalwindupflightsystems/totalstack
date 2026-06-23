def handler(store, request: dict) -> dict:
    record = store.create_virtual_node(request["meshName"], request["virtualNodeName"], request["spec"], request.get("tags"), request.get("meshOwner"))
    return record.to_dict()
