def handler(store, request: dict) -> dict:
    record = store.describe_mesh(request["meshName"], request.get("meshOwner"))
    return record.to_dict()
