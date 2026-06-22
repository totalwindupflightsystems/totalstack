def create_resolver(store, request):
    args = {k: v for k, v in request.items()
            if k not in ('apiId','typeName','fieldName')}
    return store.create_resolver(request['apiId'], request['typeName'], request['fieldName'], **args)
