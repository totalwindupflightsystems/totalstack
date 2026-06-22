def delete_collection(store, request):
    args = {k: v for k, v in request.items() if k != "id"}
    return store.delete_collection(request["id"], **args)
