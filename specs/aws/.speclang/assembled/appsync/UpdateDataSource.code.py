def update_data_source(store, request):
    args = {k: v for k, v in request.items()
            if k not in ('apiId','name','type')}
    return store.update_data_source(request['apiId'], request['name'], request['type'], **args)
