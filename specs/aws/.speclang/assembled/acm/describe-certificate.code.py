def handler(store, request: dict) -> dict:
    return store.describe_certificate(CertificateArn=request["CertificateArn"])
