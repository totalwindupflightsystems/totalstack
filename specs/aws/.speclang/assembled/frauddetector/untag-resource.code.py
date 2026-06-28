def handler(store, r: dict) -> dict:
    store.untag_resource(r["resourceARN"], r["tagKeys"])
    return {}
