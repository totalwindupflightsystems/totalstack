def handler(store, request: dict) -> dict:
    record = store.update_mesh(request["meshName"], request.get("spec"))
    return record.to_dict()
