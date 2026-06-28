def handler(store, r: dict) -> dict:
    parts = r["rule"].split("/")
    store.delete_rule(parts[1], parts[0])
    return {}
