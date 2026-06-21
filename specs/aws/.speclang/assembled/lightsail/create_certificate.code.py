# spec:trace: aws/lightsail/create_certificate.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-certificate
# spec:generated: DO NOT EDIT — edit the spec instead

def create_certificate(store, request: dict) -> dict:
    """Creates an SSL/TLS certificate for an Amazon Lightsail content delivery network (CDN) distribution and a container service. After the certificate is valid, use the AttachCertificateToDistribution acti"""
    certificate_name = request.get("certificateName", "").strip() if isinstance(request.get("certificateName"), str) else request.get("certificateName")
    if not certificate_name:
        raise ValidationException("certificateName is required")
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")
    if not domain_name:
        raise ValidationException("domainName is required")

    if store.certificates(domain_name):
        raise ResourceInUseException("Resource domain_name already exists")

    record = {
        "certificateName": certificate_name,
        "domainName": domain_name,
        "subjectAlternativeNames": subject_alternative_names,
        "tags": tags,
    }

    store.certificates(domain_name, record)

    return {
        "certificate": record.get("certificate", {}),
        "operations": record.get("operations", {}),
    }

