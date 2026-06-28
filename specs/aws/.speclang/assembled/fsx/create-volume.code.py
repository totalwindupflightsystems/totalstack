def handler(store, request: dict) -> dict:
    if not request.get("VolumeType"):
        raise BadRequest("VolumeType is required")
    if not request.get("Name"):
        raise BadRequest("Name is required")
    record = store.create_volume(**request)
    return record.to_dict()
