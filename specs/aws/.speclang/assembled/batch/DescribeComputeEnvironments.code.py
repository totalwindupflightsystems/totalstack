def handler(store, request: dict) -> dict:
    return store.describe_compute_environments(
        compute_environments=request.get("computeEnvironments"),
        max_results=request.get("maxResults"),
        next_token=request.get("nextToken"),
    )
