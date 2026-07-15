# spec:trace: aws/application-autoscaling/DeleteScalingPolicy.spec.py.md#implementation
# spec:id: @specs/aws/application-autoscaling/deletescalingpolicy
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_scaling_policy(store: 'AppAutoScalingStore', request: dict) -> dict:
    """Delete a scaling policy."""
    return store.delete_policy(
        request['PolicyName'],
        request['ResourceId'],
        request['ServiceNamespace'],
        request['ScalableDimension'],
    )