// spec:trace spec=/home/kara/totalstack/specs/aws/xray/UpdateTraceSegmentDestination.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def update_trace_segment_destination(store, request):
    destination = request.get('Destination', {})
    if not destination:
        raise InvalidRequestException('Destination is required')
    store.segment_destination = destination
    return {'Destination': destination}