def handler(store, request: dict) -> dict:
    if not request.get("FileSystemId"):
        raise BadRequest("FileSystemId is required")
    if not request.get("Name"):
        raise BadRequest("Name is required")
    record = store.create_storage_virtual_machine(**request)
    return record.to_dict()
