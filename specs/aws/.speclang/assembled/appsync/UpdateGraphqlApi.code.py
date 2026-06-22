def update_graphql_api(store, request):
    name = request['name']
    auth = request['authenticationType']
    args = {k: v for k, v in request.items()
            if k not in ('apiId','name','authenticationType')}
    return store.update_graphql_api(request['apiId'], name, auth, **args)
