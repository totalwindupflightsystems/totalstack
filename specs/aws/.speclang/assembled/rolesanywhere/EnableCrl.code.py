def handler(store, request):
    record = store.enable_crl(request["crlId"])
    return {"crl": record.to_dict()}
