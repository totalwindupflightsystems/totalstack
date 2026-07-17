def handler(store, r: dict) -> dict:
    return store.get_parameter(r["Name"], r.get("WithDecryption", False))