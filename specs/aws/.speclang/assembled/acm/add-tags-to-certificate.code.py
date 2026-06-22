def handler(store, request: dict) -> dict:
    return store.add_tags_to_certificate(
        CertificateArn=request["CertificateArn"],
        Tags=request["Tags"],
    )
