def handler(store, r: dict) -> dict:
    items = store.rules(r.get("detectorId", ""))
    return {"rules": [ru.to_dict() for ru in items], "nextToken": ""}
