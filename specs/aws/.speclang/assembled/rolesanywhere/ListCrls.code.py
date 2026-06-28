def handler(store, request):
    items = store.crls()
    return {"crls": [r.to_dict() for r in items]}
