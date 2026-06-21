# spec:trace: aws/lightsail/attach_instances_to_load_balancer.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/attach-instances-to-load-balancer
# spec:generated: DO NOT EDIT — edit the spec instead

def attach_instances_to_load_balancer(store, request: dict) -> dict:
    """Attaches one or more Lightsail instances to a load balancer. After some time, the instances are attached to the load balancer and the health check status is available. The attach instances to load bal"""
    instance_names = request.get("instanceNames", "").strip() if isinstance(request.get("instanceNames"), str) else request.get("instanceNames")
    if not instance_names:
        raise ValidationException("instanceNames is required")
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachInstancesToLoadBalancer", request)

