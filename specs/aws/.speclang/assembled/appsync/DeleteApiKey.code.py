def delete_api_key(store, request):
    return store.delete_api_key(apiId=request['apiId'], id=request['id'])
