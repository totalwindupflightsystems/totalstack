def update_collection(store, request):
    args = {k: v for k, v in request.items() if k != "id"}
    return store.update_collection(request["id"], **args)
