def list_data_sources(store, request):
    args = {k: v for k, v in request.items() if k != 'apiId'}
    return store.list_data_sources(apiId=request['apiId'], **args)
