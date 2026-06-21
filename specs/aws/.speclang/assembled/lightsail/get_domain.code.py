# spec:trace: aws/lightsail/get_domain.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-domain
# spec:generated: DO NOT EDIT — edit the spec instead

def get_domain(store, request: dict) -> dict:
    """Returns information about a specific domain recordset."""
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")
    if not domain_name:
        raise ValidationException("domainName is required")

    resource = store.domains(domain_name)
    if not resource:
        raise ResourceNotFoundException("Resource domain_name not found")
    return {"domainName": domain_name, **resource}

