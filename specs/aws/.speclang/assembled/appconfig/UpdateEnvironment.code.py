def update_environment(store, request):
    args={k:v for k,v in request.items() if k not in ('applicationId','environmentId')}
    return store.update_environment(request['applicationId'], request['environmentId'], **args)
