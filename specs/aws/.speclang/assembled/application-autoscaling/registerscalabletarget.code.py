# spec:trace: aws/application-autoscaling/RegisterScalableTarget.spec.py.md#implementation
# spec:id: @specs/aws/application-autoscaling/registerscalabletarget
# spec:generated: DO NOT EDIT — edit the spec instead

def register_scalable_target(store: 'AppAutoScalingStore', request: dict) -> dict:
    """Register or update a scalable target."""
    return store.register_target(
        request['ResourceId'],
        request['ServiceNamespace'],
        request['ScalableDimension'],
        request['MinCapacity'],
        request['MaxCapacity'],
    )