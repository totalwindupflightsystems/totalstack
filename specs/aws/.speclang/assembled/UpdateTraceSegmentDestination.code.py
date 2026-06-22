
def update_trace_segment_destination(store, request):
    destination = request.get('Destination', {})
    if not destination:
        raise InvalidRequestException('Destination is required')
    store.segment_destination = destination
    return {'Destination': destination}
