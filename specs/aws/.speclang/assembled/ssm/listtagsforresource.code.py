def handler(store, r: dict) -> dict:
    return store.list_tags(r["ResourceId"])