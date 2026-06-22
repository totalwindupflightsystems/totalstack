def handler(store, request: dict) -> dict:
    return store.update_certificate_options(
        CertificateArn=request["CertificateArn"],
        Options=request["Options"],
    )
