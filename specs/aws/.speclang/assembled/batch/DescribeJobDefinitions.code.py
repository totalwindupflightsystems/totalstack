def handler(store, request: dict) -> dict:
    return store.describe_job_definitions(
        job_definitions=request.get("jobDefinitions"),
        job_definition_name=request.get("jobDefinitionName"),
        status=request.get("status"),
        max_results=request.get("maxResults"),
        next_token=request.get("nextToken"),
    )
