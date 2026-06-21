# spec:trace: aws/lightsail/create_load_balancer.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-load-balancer
# spec:generated: DO NOT EDIT — edit the spec instead

def create_load_balancer(store, request: dict) -> dict:
    """Creates a Lightsail load balancer. To learn more about deciding whether to load balance your application, see Configure your Lightsail instances for load balancing . You can create up to 10 load balan"""
    instance_port = request.get("instancePort", "").strip() if isinstance(request.get("instancePort"), str) else request.get("instancePort")
    if not instance_port:
        raise ValidationException("instancePort is required")
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    if store.load_balancers(load_balancer_name):
        raise ResourceInUseException("Resource load_balancer_name already exists")

    health_check_path = request.get("healthCheckPath", "/")
    certificate_name = request.get("certificateName", "")
    certificate_domain_name = request.get("certificateDomainName", "")
    certificate_alternative_names = request.get("certificateAlternativeNames", [])
    tags = request.get("tags", [])
    ip_address_type = request.get("ipAddressType", "ipv4")
    tls_policy_name = request.get("tlsPolicyName", "")

    record = {
        "loadBalancerName": load_balancer_name,
        "instancePort": instance_port,
        "healthCheckPath": health_check_path,
        "certificateName": certificate_name,
        "certificateDomainName": certificate_domain_name,
        "certificateAlternativeNames": certificate_alternative_names,
        "tags": tags,
        "ipAddressType": ip_address_type,
        "tlsPolicyName": tls_policy_name,
    }

    store.load_balancers(load_balancer_name, record)

    return {
        "operations": record.get("operations", {}),
    }

