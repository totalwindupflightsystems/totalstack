def handler(store, r: dict) -> dict:
    return store.add_tags(r["ResourceId"], r["Tags"])