def handler(store, request: dict) -> dict:
    return store.describe_job_queues(
        job_queues=request.get("jobQueues"),
        max_results=request.get("maxResults"),
        next_token=request.get("nextToken"),
    )
