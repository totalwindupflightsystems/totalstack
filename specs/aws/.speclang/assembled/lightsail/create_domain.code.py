# spec:trace: aws/lightsail/create_domain.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-domain
# spec:generated: DO NOT EDIT — edit the spec instead

def create_domain(store, request: dict) -> dict:
    """Creates a domain resource for the specified domain (example.com). The create domain operation supports tag-based access control via request tags. For more information, see the Amazon Lightsail Develop"""
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")
    if not domain_name:
        raise ValidationException("domainName is required")

    if store.domains(domain_name):
        raise ResourceInUseException("Resource domain_name already exists")

    tags = request.get("tags", [])

    record = {
        "domainName": domain_name,
        "tags": tags,
    }

    store.domains(domain_name, record)

    return {
        "operation": record.get("operation", {}),
    }

