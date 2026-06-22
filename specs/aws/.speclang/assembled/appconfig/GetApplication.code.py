def get_application(store, request):
    return store.get_application(applicationId=request['applicationId'])
