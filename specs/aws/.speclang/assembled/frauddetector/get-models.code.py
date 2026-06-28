def handler(store, r: dict) -> dict:
    items = store.models()
    return {"models": [m.to_dict() for m in items], "nextToken": ""}
