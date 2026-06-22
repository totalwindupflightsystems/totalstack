def handler(store, request: dict) -> dict:
    return store.untag_resource(**request)

