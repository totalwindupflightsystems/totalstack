def handler(store, request: dict) -> dict:
    record = store.delete_mesh(request["meshName"])
    return record.to_dict()
