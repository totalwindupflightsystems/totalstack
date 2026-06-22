def handler(store, request: dict) -> dict:
    return store.revoke_certificate(
        CertificateArn=request["CertificateArn"],
        RevocationReason=request["RevocationReason"],
    )
