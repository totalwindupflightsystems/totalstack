def handler(store, request: dict) -> dict:
    record = store.delete_virtual_node(request["meshName"], request["virtualNodeName"], request.get("meshOwner"))
    return record.to_dict()
