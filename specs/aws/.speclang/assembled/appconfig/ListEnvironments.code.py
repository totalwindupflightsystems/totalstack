def list_environments(store, request):
    args={k:v for k,v in request.items() if k!='applicationId'}
    return store.list_environments(request['applicationId'], **args)
