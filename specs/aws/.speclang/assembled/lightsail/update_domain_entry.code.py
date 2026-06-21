# spec:trace: aws/lightsail/update_domain_entry.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/update-domain-entry
# spec:generated: DO NOT EDIT — edit the spec instead

def update_domain_entry(store, request: dict) -> dict:
    """Updates a domain recordset after it is created. The update domain entry operation supports tag-based access control via resource tags applied to the resource identified by domain name . For more infor"""
    domain_entry = request.get("domainEntry", "").strip() if isinstance(request.get("domainEntry"), str) else request.get("domainEntry")
    if not domain_entry:
        raise ValidationException("domainEntry is required")
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")
    if not domain_name:
        raise ValidationException("domainName is required")

    resource = store.domain_entrys(domain_name)
    if not resource:
        raise ResourceNotFoundException("Resource domain_name not found")

    # Update mutable fields

    store.domain_entrys(domain_name, resource)
    return resource

