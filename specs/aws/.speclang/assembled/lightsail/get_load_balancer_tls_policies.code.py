# spec:trace: aws/lightsail/get_load_balancer_tls_policies.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-load-balancer-tls-policies
# spec:generated: DO NOT EDIT — edit the spec instead

def get_load_balancer_tls_policies(store, request: dict) -> dict:
    """Returns a list of TLS security policies that you can apply to Lightsail load balancers. For more information about load balancer TLS security policies, see Configuring TLS security policies on your Am"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

