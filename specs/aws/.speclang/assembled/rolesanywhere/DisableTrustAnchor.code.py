def handler(store, request):
    record = store.disable_trust_anchor(request["trustAnchorId"])
    return {"trustAnchor": record.to_dict()}
