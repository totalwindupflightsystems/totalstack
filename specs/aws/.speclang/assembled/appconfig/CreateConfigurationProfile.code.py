def create_configuration_profile(store, request):
    args={k:v for k,v in request.items() if k not in ('applicationId','name','locationUri')}
    return store.create_configuration_profile(request['applicationId'], request['name'], request.get('locationUri',''), **args)
