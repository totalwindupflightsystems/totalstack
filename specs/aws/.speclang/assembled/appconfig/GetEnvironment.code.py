def get_environment(store, request):
    return store.get_environment(applicationId=request['applicationId'], environmentId=request['environmentId'])
