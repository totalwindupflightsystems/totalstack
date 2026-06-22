def create_collection(store, request):
    args = {k: v for k, v in request.items() if k != "name"}
    return store.create_collection(request.get("name", ""), **args)
