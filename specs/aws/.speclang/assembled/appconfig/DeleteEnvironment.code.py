def delete_environment(store, request):
    return store.delete_environment(applicationId=request['applicationId'], environmentId=request['environmentId'])
