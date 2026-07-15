# spec:trace: aws/application-autoscaling/DescribeScalableTargets.spec.py.md#implementation
# spec:id: @specs/aws/application-autoscaling/describescalabletargets
# spec:generated: DO NOT EDIT — edit the spec instead

def describe_scalable_targets(store: 'AppAutoScalingStore', request: dict) -> dict:
    """Describe scalable targets."""
    return store.describe_targets(
        namespace=request.get('ServiceNamespace'),
        resource_ids=request.get('ResourceIds'),
        dimension=request.get('ScalableDimension'),
    )