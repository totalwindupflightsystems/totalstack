# spec:trace: aws/lightsail/delete_domain_entry.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-domain-entry
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_domain_entry(store, request: dict) -> dict:
    """Deletes a specific domain entry. The delete domain entry operation supports tag-based access control via resource tags applied to the resource identified by domain name . For more information, see the"""
    request.get("domainEntry", "").strip() if isinstance(request.get("domainEntry"), str) else request.get("domainEntry")
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")

    if not store.domain_entrys(domain_name):
        raise ResourceNotFoundException("Resource domain_name not found")
    store.delete_domain_entrys(domain_name)
    return {}

