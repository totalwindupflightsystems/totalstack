
def get_trace_segment_destination(store, request):
    dest = store.segment_destination or {'Type': 'XRay', 'Status': 'ACTIVE'}
    return {'Destination': dest}
