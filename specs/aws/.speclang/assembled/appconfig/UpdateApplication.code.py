def update_application(store, request):
    args={k:v for k,v in request.items() if k!='applicationId'}
    return store.update_application(request['applicationId'], **args)
