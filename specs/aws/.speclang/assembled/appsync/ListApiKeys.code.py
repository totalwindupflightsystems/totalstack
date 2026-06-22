def list_api_keys(store, request):
    return store.list_api_keys(apiId=request['apiId'])
