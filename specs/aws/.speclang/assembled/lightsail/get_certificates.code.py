# spec:trace: aws/lightsail/get_certificates.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-certificates
# spec:generated: DO NOT EDIT — edit the spec instead

def get_certificates(store, request: dict) -> dict:
    """Returns information about one or more Amazon Lightsail SSL/TLS certificates. To get a summary of a certificate, omit includeCertificateDetails from your request. The response will include only the cer"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

