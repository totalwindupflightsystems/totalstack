def handler(store, r: dict) -> dict:
    return store.get_parameters(r["Names"], r.get("WithDecryption", False))