def handler(store, request: dict) -> dict:
    return store.query(request['IndexId'], request['QueryText'])

