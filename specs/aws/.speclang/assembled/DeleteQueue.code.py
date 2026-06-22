
def execute_delete_queue(store, request):
    """Delete a queue."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")

    if name not in store.queues:
        raise ResourceNotFoundException(f"Queue '{name}' not found")

    del store.queues[name]

    return {}
