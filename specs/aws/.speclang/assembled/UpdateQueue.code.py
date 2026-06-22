
def execute_update_queue(store, request):
    """Update an existing queue."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")

    q = store.queues.get(name)
    if not q:
        raise ResourceNotFoundException(f"Queue '{name}' not found")

    if 'Description' in request:
        q.description = request['Description']
    if 'Status' in request:
        q.status = request['Status']
    if 'ConcurrentJobs' in request:
        q.concurrent_jobs = request['ConcurrentJobs']

    q.last_updated = time.time()

    return {"Queue": q.to_dict()}
