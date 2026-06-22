def handler(store, request: dict) -> dict:
    return store.request_certificate(
        DomainName=request["DomainName"],
        SubjectAlternativeNames=request.get("SubjectAlternativeNames"),
        ValidationMethod=request.get("ValidationMethod", "EMAIL"),
        Options=request.get("Options"),
        IdempotencyToken=request.get("IdempotencyToken"),
        CertificateAuthorityArn=request.get("CertificateAuthorityArn"),
        Tags=request.get("Tags"),
        KeyAlgorithm=request.get("KeyAlgorithm", "RSA_2048"),
    )
