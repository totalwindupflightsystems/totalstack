# spec:trace: aws/lightsail/detach_certificate_from_distribution.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/detach-certificate-from-distribution
# spec:generated: DO NOT EDIT — edit the spec instead

def detach_certificate_from_distribution(store, request: dict) -> dict:
    """Detaches an SSL/TLS certificate from your Amazon Lightsail content delivery network (CDN) distribution. After the certificate is detached, your distribution stops accepting traffic for all of the doma"""
    distribution_name = request.get("distributionName", "").strip() if isinstance(request.get("distributionName"), str) else request.get("distributionName")
    if not distribution_name:
        raise ValidationException("distributionName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetachCertificateFromDistribution", request)

