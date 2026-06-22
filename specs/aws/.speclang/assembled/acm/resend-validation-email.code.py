def handler(store, request: dict) -> dict:
    return store.resend_validation_email(
        CertificateArn=request["CertificateArn"],
        Domain=request["Domain"],
        ValidationDomain=request["ValidationDomain"],
    )
