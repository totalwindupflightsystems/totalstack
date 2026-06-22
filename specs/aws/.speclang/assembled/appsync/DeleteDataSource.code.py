def delete_data_source(store, request):
    return store.delete_data_source(apiId=request['apiId'], name=request['name'])
