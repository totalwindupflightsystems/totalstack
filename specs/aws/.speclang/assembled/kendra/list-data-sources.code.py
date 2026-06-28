def handler(store, request: dict) -> dict:
    return store.list_data_sources(request['IndexId'])

