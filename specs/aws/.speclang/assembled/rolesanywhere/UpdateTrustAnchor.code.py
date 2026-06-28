def handler(store, request):
    record = store.update_trust_anchor(
        request["trustAnchorId"],
        name=request.get("name"),
        source=request.get("source"),
    )
    return {"trustAnchor": record.to_dict()}
