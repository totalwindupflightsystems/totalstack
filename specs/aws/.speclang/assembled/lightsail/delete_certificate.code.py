# spec:trace: aws/lightsail/delete_certificate.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-certificate
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_certificate(store, request: dict) -> dict:
    """Deletes an SSL/TLS certificate for your Amazon Lightsail content delivery network (CDN) distribution. Certificates that are currently attached to a distribution cannot be deleted. Use the DetachCertif"""
    certificate_name = request.get("certificateName", "").strip() if isinstance(request.get("certificateName"), str) else request.get("certificateName")

    if not store.certificates(certificate_name):
        raise ResourceNotFoundException("Resource certificate_name not found")
    store.delete_certificates(certificate_name)
    return {}

