def handler(store, request: dict) -> dict:
    return store.describe_data_source(request['Id'], request['IndexId'])

