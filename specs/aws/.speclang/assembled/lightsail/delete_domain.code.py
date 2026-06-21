# spec:trace: aws/lightsail/delete_domain.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-domain
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_domain(store, request: dict) -> dict:
    """Deletes the specified domain recordset and all of its domain records. The delete domain operation supports tag-based access control via resource tags applied to the resource identified by domain name """
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")

    if not store.domains(domain_name):
        raise ResourceNotFoundException("Resource domain_name not found")
    store.delete_domains(domain_name)
    return {}

