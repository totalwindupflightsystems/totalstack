# spec:trace: aws/lightsail/attach_certificate_to_distribution.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/attach-certificate-to-distribution
# spec:generated: DO NOT EDIT — edit the spec instead

def attach_certificate_to_distribution(store, request: dict) -> dict:
    """Attaches an SSL/TLS certificate to your Amazon Lightsail content delivery network (CDN) distribution. After the certificate is attached, your distribution accepts HTTPS traffic for all of the domains """
    certificate_name = request.get("certificateName", "").strip() if isinstance(request.get("certificateName"), str) else request.get("certificateName")
    if not certificate_name:
        raise ValidationException("certificateName is required")
    distribution_name = request.get("distributionName", "").strip() if isinstance(request.get("distributionName"), str) else request.get("distributionName")
    if not distribution_name:
        raise ValidationException("distributionName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachCertificateToDistribution", request)

