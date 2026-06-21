# spec:trace: aws/lightsail/setup_instance_https.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/setup-instance-https
# spec:generated: DO NOT EDIT — edit the spec instead

def setup_instance_https(store, request: dict) -> dict:
    """Creates an SSL/TLS certificate that secures traffic for your website. After the certificate is created, it is installed on the specified Lightsail instance. If you provide more than one domain name in"""
    certificate_provider = request.get("certificateProvider", "").strip() if isinstance(request.get("certificateProvider"), str) else request.get("certificateProvider")
    if not certificate_provider:
        raise ValidationException("certificateProvider is required")
    domain_names = request.get("domainNames", "").strip() if isinstance(request.get("domainNames"), str) else request.get("domainNames")
    if not domain_names:
        raise ValidationException("domainNames is required")
    email_address = request.get("emailAddress", "").strip() if isinstance(request.get("emailAddress"), str) else request.get("emailAddress")
    if not email_address:
        raise ValidationException("emailAddress is required")
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    resource = store.setup_instance_httpss(certificate_provider)
    if not resource:
        raise ResourceNotFoundException("Resource certificate_provider not found")

    # Update mutable fields

    store.setup_instance_httpss(certificate_provider, resource)
    return resource

