def handler(store, r: dict) -> dict:
    store.tag_resource(r["resourceARN"], r["tags"])
    return {}
