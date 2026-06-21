# spec:trace: aws/lightsail/create_load_balancer_tls_certificate.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-load-balancer-tls-certificate
# spec:generated: DO NOT EDIT — edit the spec instead

def create_load_balancer_tls_certificate(store, request: dict) -> dict:
    """Creates an SSL/TLS certificate for an Amazon Lightsail load balancer. TLS is just an updated, more secure version of Secure Socket Layer (SSL). The CreateLoadBalancerTlsCertificate operation supports """
    certificate_domain_name = request.get("certificateDomainName", "").strip() if isinstance(request.get("certificateDomainName"), str) else request.get("certificateDomainName")
    if not certificate_domain_name:
        raise ValidationException("certificateDomainName is required")
    certificate_name = request.get("certificateName", "").strip() if isinstance(request.get("certificateName"), str) else request.get("certificateName")
    if not certificate_name:
        raise ValidationException("certificateName is required")
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    if store.load_balancer_tls_certificates(certificate_domain_name):
        raise ResourceInUseException("Resource certificate_domain_name already exists")

    record = {
        "loadBalancerName": load_balancer_name,
        "certificateName": certificate_name,
        "certificateDomainName": certificate_domain_name,
        "certificateAlternativeNames": certificate_alternative_names,
        "tags": tags,
    }

    store.load_balancer_tls_certificates(certificate_domain_name, record)

    return {
        "operations": record.get("operations", {}),
    }

