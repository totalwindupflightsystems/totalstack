def handler(store, request):
    items = store.profiles()
    return {"profiles": [r.to_dict() for r in items]}
