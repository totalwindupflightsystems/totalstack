def handler(store, request: dict) -> dict:
    return store.remove_tags_from_certificate(
        CertificateArn=request["CertificateArn"],
        Tags=request["Tags"],
    )
