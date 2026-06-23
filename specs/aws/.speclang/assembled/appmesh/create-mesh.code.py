def handler(store, request: dict) -> dict:
    record = store.create_mesh(request["meshName"], request.get("spec"), request.get("tags"))
    return record.to_dict()
