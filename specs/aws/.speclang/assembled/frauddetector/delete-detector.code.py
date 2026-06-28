def handler(store, r: dict) -> dict:
    store.delete_detector(r["detectorId"])
    return {}
