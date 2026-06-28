def handler(store, request: dict) -> dict:
    store.delete_file_cache(request["FileCacheId"])
    return {}
