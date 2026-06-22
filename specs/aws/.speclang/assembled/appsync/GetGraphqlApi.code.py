def get_graphql_api(store, request):
    return store.get_graphql_api(apiId=request['apiId'])
