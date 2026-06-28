def handler(store, request):
    record = store.crls(request["crlId"])
    if not record:
        raise ResourceNotFoundException(f"CRL {request['crlId']} not found")
    return {"crl": record.to_dict()}
