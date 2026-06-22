def handler(store, request: dict) -> dict:
    return store.import_certificate(
        Certificate=request["Certificate"],
        PrivateKey=request["PrivateKey"],
        CertificateChain=request.get("CertificateChain"),
        CertificateArn=request.get("CertificateArn"),
        Tags=request.get("Tags"),
    )
