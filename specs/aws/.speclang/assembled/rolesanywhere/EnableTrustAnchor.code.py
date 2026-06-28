def handler(store, request):
    record = store.enable_trust_anchor(request["trustAnchorId"])
    return {"trustAnchor": record.to_dict()}
