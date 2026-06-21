# spec:trace: aws/lightsail/detach_instances_from_load_balancer.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/detach-instances-from-load-balancer
# spec:generated: DO NOT EDIT — edit the spec instead

def detach_instances_from_load_balancer(store, request: dict) -> dict:
    """Detaches the specified instances from a Lightsail load balancer. This operation waits until the instances are no longer needed before they are detached from the load balancer. The detach instances fro"""
    instance_names = request.get("instanceNames", "").strip() if isinstance(request.get("instanceNames"), str) else request.get("instanceNames")
    if not instance_names:
        raise ValidationException("instanceNames is required")
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetachInstancesFromLoadBalancer", request)

