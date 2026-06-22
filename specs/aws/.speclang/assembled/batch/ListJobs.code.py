def handler(store, request: dict) -> dict:
    return store.list_jobs(
        job_queue=request.get("jobQueue"),
        array_job_id=request.get("arrayJobId"),
        job_status=request.get("jobStatus"),
        max_results=request.get("maxResults"),
        next_token=request.get("nextToken"),
        filters=request.get("filters"),
    )
