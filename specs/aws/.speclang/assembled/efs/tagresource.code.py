def handler(store, r: dict) -> dict:
    return store.tag_resource(r['ResourceId'], r['Tags'])