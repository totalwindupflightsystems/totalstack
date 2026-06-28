def handler(store, request):
    record = store.delete_crl(request["crlId"])
    return {"crl": record.to_dict()}
