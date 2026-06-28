def handler(store, r: dict) -> dict:
    items = store.detectors()
    return {"detectors": [d.to_dict() for d in items], "nextToken": ""}
