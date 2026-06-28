def handler(store, request):
    record = store.trust_anchors(request["trustAnchorId"])
    if not record:
        raise ResourceNotFoundException(f"Trust anchor {request['trustAnchorId']} not found")
    return {"trustAnchor": record.to_dict()}
