def handler(store, r: dict) -> dict:
    items = store.eventtypes()
    return {"eventTypes": [e.to_dict() for e in items], "nextToken": ""}
