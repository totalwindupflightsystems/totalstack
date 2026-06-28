def handler(store, request):
    record = store.update_crl(
        request["crlId"],
        name=request.get("name"),
        crlData=request.get("crlData"),
    )
    return {"crl": record.to_dict()}
