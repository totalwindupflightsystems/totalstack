# spec:trace: aws/application-autoscaling/PutScalingPolicy.spec.py.md#implementation
# spec:id: @specs/aws/application-autoscaling/putscalingpolicy
# spec:generated: DO NOT EDIT — edit the spec instead

def put_scaling_policy(store: 'AppAutoScalingStore', request: dict) -> dict:
    """Create or update a scaling policy."""
    return store.put_policy(
        request['PolicyName'],
        request['ResourceId'],
        request['ServiceNamespace'],
        request['ScalableDimension'],
        request['PolicyType'],
    )