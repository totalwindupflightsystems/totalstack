# spec:trace: aws/lightsail/create_domain_entry.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-domain-entry
# spec:generated: DO NOT EDIT — edit the spec instead

def create_domain_entry(store, request: dict) -> dict:
    """Creates one of the following domain name system (DNS) records in a domain DNS zone: Address (A), canonical name (CNAME), mail exchanger (MX), name server (NS), start of authority (SOA), service locato"""
    domain_entry = request.get("domainEntry", "").strip() if isinstance(request.get("domainEntry"), str) else request.get("domainEntry")
    if not domain_entry:
        raise ValidationException("domainEntry is required")
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")
    if not domain_name:
        raise ValidationException("domainName is required")

    if store.domain_entrys(domain_name):
        raise ResourceInUseException("Resource domain_name already exists")

    record = {
        "domainName": domain_name,
        "domainEntry": domain_entry,
    }

    store.domain_entrys(domain_name, record)

    return {
        "operation": record.get("operation", {}),
    }

