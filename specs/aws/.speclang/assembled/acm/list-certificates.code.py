def handler(store, request: dict) -> dict:
    return store.list_certificates(
        CertificateStatuses=request.get("CertificateStatuses"),
        Includes=request.get("Includes"),
        NextToken=request.get("NextToken"),
        MaxItems=request.get("MaxItems", 50),
    )
