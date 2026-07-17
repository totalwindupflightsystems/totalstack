def handler(store, r: dict) -> dict:
    return store.remove_tags(r["ResourceId"], r["TagKeys"])