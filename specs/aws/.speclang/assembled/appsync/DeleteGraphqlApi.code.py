def delete_graphql_api(store, request):
    return store.delete_graphql_api(apiId=request['apiId'])
