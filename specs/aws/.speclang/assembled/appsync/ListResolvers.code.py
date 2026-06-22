def list_resolvers(store, request):
    args = {k: v for k, v in request.items() if k not in ('apiId', 'typeName')}
    return store.list_resolvers(request['apiId'], request['typeName'], **args)
