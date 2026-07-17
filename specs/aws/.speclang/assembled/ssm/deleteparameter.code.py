def handler(store, r: dict) -> dict:
    return store.delete_parameter(r["Name"])