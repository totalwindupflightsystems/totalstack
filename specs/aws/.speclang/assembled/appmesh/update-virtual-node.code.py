def handler(store, request: dict) -> dict:
    record = store.update_virtual_node(request["meshName"], request["virtualNodeName"], request["spec"], request.get("meshOwner"))
    return record.to_dict()
