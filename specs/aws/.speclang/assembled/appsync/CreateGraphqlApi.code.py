def create_graphql_api(store, request):
    name = request.get('name', '')
    auth = request.get('authenticationType', 'API_KEY')
    args = {k: v for k, v in request.items() if k not in ('name','authenticationType')}
    return store.create_graphql_api(name, auth, **args)
