def delete_resolver(store, request):
    return store.delete_resolver(apiId=request['apiId'], typeName=request['typeName'], fieldName=request['fieldName'])
