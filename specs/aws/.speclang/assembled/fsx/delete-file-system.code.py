def handler(store, request: dict) -> dict:
    store.delete_file_system(request["FileSystemId"])
    return {}
