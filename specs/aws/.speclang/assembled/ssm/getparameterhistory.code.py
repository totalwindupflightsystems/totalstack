def handler(store, r: dict) -> dict:
    return store.get_parameter_history(r["Name"], r.get("MaxResults", 50))