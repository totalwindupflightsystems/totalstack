def handler(store, request):
    items = store.trust_anchors()
    return {"trustAnchors": [r.to_dict() for r in items]}
