
def execute_list_jobs(store, request):
    """List jobs with optional filters and pagination."""
    max_results = min(request.get('MaxResults', 20), 100)
    next_token = request.get('NextToken', '')
    queue_filter = request.get('Queue', '')
    status_filter = request.get('Status', '')
    order = request.get('Order', 'DESCENDING')

    all_jobs = list(store.jobs.values())

    if queue_filter:
        all_jobs = [j for j in all_jobs if j.queue == queue_filter]
    if status_filter:
        all_jobs = [j for j in all_jobs if j.status == status_filter]

    all_jobs.sort(key=lambda j: j.created_at, reverse=(order == 'DESCENDING'))

    start_idx = 0
    if next_token:
        try:
            start_idx = int(next_token)
        except ValueError:
            start_idx = 0

    page = all_jobs[start_idx:start_idx + max_results]

    result = {"Jobs": [j.to_dict() for j in page]}
    if start_idx + max_results < len(all_jobs):
        result["NextToken"] = str(start_idx + max_results)

    return result
