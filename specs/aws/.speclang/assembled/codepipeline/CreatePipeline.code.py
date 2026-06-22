def handler(store, request: dict) -> dict:
    pipeline = request["pipeline"]
    return store.create_pipeline(
        name=pipeline["name"],
        role_arn=pipeline["roleArn"],
        stages=pipeline["stages"],
        artifact_store=pipeline.get("artifactStore"),
        artifact_stores=pipeline.get("artifactStores"),
        execution_mode=pipeline.get("executionMode", "SUPERSEDED"),
        pipeline_type=pipeline.get("pipelineType", "V1"),
        tags=request.get("tags"),
    )
