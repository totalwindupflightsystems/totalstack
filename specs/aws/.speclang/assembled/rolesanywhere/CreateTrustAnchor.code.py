def handler(store, request):
    record = store.create_trust_anchor(
        name=request["name"],
        source=request.get("source"),
        enabled=request.get("enabled", True),
        tags=request.get("tags"),
    )
    return {"trustAnchor": record.to_dict()}
