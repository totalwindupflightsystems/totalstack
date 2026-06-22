def delete_configuration_profile(store, request):
    return store.delete_configuration_profile(applicationId=request['applicationId'], configurationProfileId=request['configurationProfileId'])
