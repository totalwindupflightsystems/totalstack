def handler(store, request: dict) -> dict:
    return store.delete_data_source(request['Id'], request['IndexId'])

