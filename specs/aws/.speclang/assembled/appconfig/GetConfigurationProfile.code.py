def get_configuration_profile(store, request):
    return store.get_configuration_profile(applicationId=request['applicationId'], configurationProfileId=request['configurationProfileId'])
