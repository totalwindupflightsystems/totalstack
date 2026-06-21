// spec:trace spec=/home/kara/totalstack/specs/aws/mediaconvert/GetQueue.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def execute_get_queue(store, request):
    """Get a queue by name."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")
    
    q = store.queues.get(name)
    if not q:
        raise ResourceNotFoundException(f"Queue '{name}' not found")
    
    return {"Queue": q.to_dict()}