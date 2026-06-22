def update_configuration_profile(store, request):
    args={k:v for k,v in request.items() if k not in ('applicationId','configurationProfileId')}
    return store.update_configuration_profile(request['applicationId'], request['configurationProfileId'], **args)
