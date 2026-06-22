def handler(store, request: dict) -> dict:
    return store.get_pipeline_execution(
        pipeline_name=request["pipelineName"],
        pipeline_execution_id=request["pipelineExecutionId"],
    )
