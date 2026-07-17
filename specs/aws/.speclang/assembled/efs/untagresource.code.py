def handler(store, r: dict) -> dict:
    return store.untag_resource(r['ResourceId'], r['TagKeys'])