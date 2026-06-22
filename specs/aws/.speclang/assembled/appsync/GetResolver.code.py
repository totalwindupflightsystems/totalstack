def get_resolver(store, request):
    return store.get_resolver(apiId=request['apiId'], typeName=request['typeName'], fieldName=request['fieldName'])
