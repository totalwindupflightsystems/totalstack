def update_api_key(store, request):
    args = {k: v for k, v in request.items() if k not in ('apiId','id')}
    return store.update_api_key(request['apiId'], request['id'], **args)
