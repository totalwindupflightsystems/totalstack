def get_data_source(store, request):
    return store.get_data_source(apiId=request['apiId'], name=request['name'])
