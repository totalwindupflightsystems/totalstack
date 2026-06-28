def handler(store, r: dict) -> dict:
    items = store.variables()
    return {"variables": [v.to_dict() for v in items], "nextToken": ""}
