def handler(store, request: dict) -> dict:
    return store.stop_pipeline_execution(
        pipeline_name=request["pipelineName"],
        pipeline_execution_id=request["pipelineExecutionId"],
        abandon=request.get("abandon", False),
        reason=request.get("reason"),
    )
