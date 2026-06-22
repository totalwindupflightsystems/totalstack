def handler(store, request: dict) -> dict:
    return store.export_certificate(
        CertificateArn=request["CertificateArn"],
        Passphrase=request["Passphrase"],
    )
