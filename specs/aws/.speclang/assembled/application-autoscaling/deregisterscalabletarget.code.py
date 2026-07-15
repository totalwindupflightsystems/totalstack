# spec:trace: aws/application-autoscaling/DeregisterScalableTarget.spec.py.md#implementation
# spec:id: @specs/aws/application-autoscaling/deregisterscalabletarget
# spec:generated: DO NOT EDIT — edit the spec instead

def deregister_scalable_target(store: 'AppAutoScalingStore', request: dict) -> dict:
    """Deregister a scalable target."""
    return store.deregister_target(
        request['ResourceId'],
        request['ServiceNamespace'],
        request['ScalableDimension'],
    )