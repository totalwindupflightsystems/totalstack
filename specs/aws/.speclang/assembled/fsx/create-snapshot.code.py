def handler(store, request: dict) -> dict:
    if not request.get("Name"):
        raise BadRequest("Name is required")
    if not request.get("VolumeId"):
        raise BadRequest("VolumeId is required")
    record = store.create_snapshot(**request)
    return record.to_dict()
