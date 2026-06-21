# spec:trace: aws/lightsail/delete_load_balancer_tls_certificate.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-load-balancer-tls-certificate
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_load_balancer_tls_certificate(store, request: dict) -> dict:
    """Deletes an SSL/TLS certificate associated with a Lightsail load balancer. The DeleteLoadBalancerTlsCertificate operation supports tag-based access control via resource tags applied to the resource ide"""
    certificate_name = request.get("certificateName", "").strip() if isinstance(request.get("certificateName"), str) else request.get("certificateName")
    request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")

    if not store.load_balancer_tls_certificates(certificate_name):
        raise ResourceNotFoundException("Resource certificate_name not found")
    store.delete_load_balancer_tls_certificates(certificate_name)
    return {}

