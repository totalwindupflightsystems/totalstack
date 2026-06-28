def handler(store, request):
    record = store.disable_crl(request["crlId"])
    return {"crl": record.to_dict()}
