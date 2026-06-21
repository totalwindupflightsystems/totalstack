# spec:trace: aws/lightsail/delete_load_balancer.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-load-balancer
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_load_balancer(store, request: dict) -> dict:
    """Deletes a Lightsail load balancer and all its associated SSL/TLS certificates. Once the load balancer is deleted, you will need to create a new load balancer, create a new certificate, and verify doma"""
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")

    if not store.load_balancers(load_balancer_name):
        raise ResourceNotFoundException("Resource load_balancer_name not found")
    store.delete_load_balancers(load_balancer_name)
    return {}

