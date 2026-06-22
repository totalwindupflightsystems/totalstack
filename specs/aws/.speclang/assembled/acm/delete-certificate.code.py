def handler(store, request: dict) -> dict:
    return store.delete_certificate(CertificateArn=request["CertificateArn"])
