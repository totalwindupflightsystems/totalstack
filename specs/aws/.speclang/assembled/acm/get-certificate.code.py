def handler(store, request: dict) -> dict:
    return store.get_certificate(CertificateArn=request["CertificateArn"])
