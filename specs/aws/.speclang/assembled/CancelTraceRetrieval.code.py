// spec:trace spec=/home/kara/totalstack/specs/aws/xray/CancelTraceRetrieval.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def cancel_trace_retrieval(store, request):
    token = request.get('RetrievalToken', '')
    if not token:
        raise InvalidRequestException('RetrievalToken is required')
    if token not in store.trace_retrievals:
        raise InvalidRequestException(f'Retrieval token not found')
    store.trace_retrievals[token]['Status'] = 'CANCELLED'
    return {}