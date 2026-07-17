def handler(store, r: dict) -> dict:
    return store.list_streams(r.get("Limit", 10), r.get("ExclusiveStartStreamName"))