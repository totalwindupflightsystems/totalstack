# spec:trace: aws/lightsail/attach_load_balancer_tls_certificate.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/attach-load-balancer-tls-certificate
# spec:generated: DO NOT EDIT — edit the spec instead

def attach_load_balancer_tls_certificate(store, request: dict) -> dict:
    """Attaches a Transport Layer Security (TLS) certificate to your load balancer. TLS is just an updated, more secure version of Secure Socket Layer (SSL). Once you create and validate your certificate, yo"""
    certificate_name = request.get("certificateName", "").strip() if isinstance(request.get("certificateName"), str) else request.get("certificateName")
    if not certificate_name:
        raise ValidationException("certificateName is required")
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachLoadBalancerTlsCertificate", request)

