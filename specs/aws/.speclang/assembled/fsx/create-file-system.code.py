def handler(store, request: dict) -> dict:
    required = ["FileSystemType", "SubnetIds"]
    for f in required:
        if not request.get(f):
            raise BadRequest(f"{f} is required")
    record = store.create_file_system(**request)
    return record.to_dict()
