// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetTraceSegmentDestination.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_trace_segment_destination(store, request):
    dest = store.segment_destination or {'Type': 'XRay', 'Status': 'ACTIVE'}
    return {'Destination': dest}