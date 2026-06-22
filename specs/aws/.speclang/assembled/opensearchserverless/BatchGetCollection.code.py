def batch_get_collection(store, request):
    return store.batch_get_collection(
        ids=request.get("ids"), names=request.get("names"))
