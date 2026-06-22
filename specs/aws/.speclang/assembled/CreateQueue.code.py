
def execute_create_queue(store, request):
    """Create a new queue."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")

    if name in store.queues:
        raise ConflictException(f"Queue '{name}' already exists")

    q = QueueRecord(
        name=name,
        Description=request.get('Description', ''),
        Status=request.get('Status', 'ACTIVE'),
        PricingPlan=request.get('PricingPlan', 'ON_DEMAND'),
        ConcurrentJobs=request.get('ConcurrentJobs', 3),
        Tags=request.get('Tags', {}),
    )

    store.queues[name] = q

    return {"Queue": q.to_dict()}
