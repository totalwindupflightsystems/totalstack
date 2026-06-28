def handler(store, request: dict) -> dict:
    return store.update_data_source(request['Id'], request['IndexId'], Name=request.get('Name'), Description=request.get('Description'))

