def batch_get_lifecycle_policy(store, request):
    return store.batch_get_lifecycle_policy(
        identifiers=request.get("identifiers", []))
