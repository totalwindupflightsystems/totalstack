def list_configuration_profiles(store, request):
    args={k:v for k,v in request.items() if k!='applicationId'}
    return store.list_configuration_profiles(request['applicationId'], **args)
