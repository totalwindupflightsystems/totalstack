def handler(store, request: dict) -> dict:
    return store.list_pipeline_executions(
        pipeline_name=request["pipelineName"],
        next_token=request.get("nextToken"),
        max_results=request.get("maxResults"),
    )
