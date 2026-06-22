def handler(store, request: dict) -> dict:
    store.delete_studio(request["StudioId"])
    return {}
