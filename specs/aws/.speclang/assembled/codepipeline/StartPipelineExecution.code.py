def handler(store, request: dict) -> dict:
    return store.start_pipeline_execution(
        name=request["name"],
        client_request_token=request.get("clientRequestToken"),
        source_revision=request.get("sourceRevision"),
        variables=request.get("variables"),
    )
