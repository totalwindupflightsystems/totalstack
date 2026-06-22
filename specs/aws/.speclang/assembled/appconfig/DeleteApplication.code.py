def delete_application(store, request):
    return store.delete_application(applicationId=request['applicationId'])
