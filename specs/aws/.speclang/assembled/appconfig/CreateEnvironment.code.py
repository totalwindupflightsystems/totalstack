def create_environment(store, request):
    args = {k: v for k, v in request.items() if k not in ('applicationId', 'name')}
    return store.create_environment(request['applicationId'], request.get('name', ''), **args)
