def handler(store, request):
    record = store.import_crl(
        name=request["name"],
        crlData=request["crlData"],
        trustAnchorArn=request.get("trustAnchorArn"),
        enabled=request.get("enabled", True),
        tags=request.get("tags"),
    )
    return {"crl": record.to_dict()}
