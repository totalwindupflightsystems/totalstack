def handler(store, r: dict) -> dict:
    store.delete_eventtype(r["name"])
    return {}
