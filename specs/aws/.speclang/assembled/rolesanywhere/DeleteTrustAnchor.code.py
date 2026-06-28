def handler(store, request):
    record = store.delete_trust_anchor(request["trustAnchorId"])
    return {"trustAnchor": record.to_dict()}
