
def execute_list_queues(store, request):
    """List queues."""
    max_results = min(request.get('MaxResults', 20), 100)
    next_token = request.get('NextToken', '')
    list_order = request.get('ListOrder', 'ASCENDING')

    all_queues = list(store.queues.values())
    all_queues.sort(key=lambda q: q.name, reverse=(list_order == 'DESCENDING'))

    start_idx = 0
    if next_token:
        try:
            start_idx = int(next_token)
        except ValueError:
            start_idx = 0

    page = all_queues[start_idx:start_idx + max_results]

    result = {"Queues": [q.to_dict() for q in page]}
    if start_idx + max_results < len(all_queues):
        result["NextToken"] = str(start_idx + max_results)

    return result
