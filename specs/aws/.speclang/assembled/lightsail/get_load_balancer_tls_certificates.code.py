# spec:trace: aws/lightsail/get_load_balancer_tls_certificates.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-load-balancer-tls-certificates
# spec:generated: DO NOT EDIT — edit the spec instead

def get_load_balancer_tls_certificates(store, request: dict) -> dict:
    """Returns information about the TLS certificates that are associated with the specified Lightsail load balancer. TLS is just an updated, more secure version of Secure Socket Layer (SSL). You can have a """
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    resource = store.load_balancer_tls_certificatess(load_balancer_name)
    if not resource:
        raise ResourceNotFoundException("Resource load_balancer_name not found")
    return {"loadBalancerName": load_balancer_name, **resource}

