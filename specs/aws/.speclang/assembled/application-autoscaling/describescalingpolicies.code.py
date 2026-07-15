# spec:trace: aws/application-autoscaling/DescribeScalingPolicies.spec.py.md#implementation
# spec:id: @specs/aws/application-autoscaling/describescalingpolicies
# spec:generated: DO NOT EDIT — edit the spec instead

def describe_scaling_policies(store: 'AppAutoScalingStore', request: dict) -> dict:
    """Describe scaling policies."""
    return store.describe_policies(
        namespace=request.get('ServiceNamespace'),
        resource_id=request.get('ResourceId'),
        names=request.get('PolicyNames'),
    )