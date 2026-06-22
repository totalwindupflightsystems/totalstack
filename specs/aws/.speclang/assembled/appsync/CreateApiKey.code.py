def create_api_key(store, request):
    args = {k: v for k, v in request.items() if k != 'apiId'}
    return store.create_api_key(request['apiId'], **args)
