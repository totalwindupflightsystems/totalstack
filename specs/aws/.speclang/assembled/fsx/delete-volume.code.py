def handler(store, request: dict) -> dict:
    store.delete_volume(request["VolumeId"])
    return {}
