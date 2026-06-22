def handler(store, request: dict) -> dict:
    return store.renew_certificate(CertificateArn=request["CertificateArn"])
