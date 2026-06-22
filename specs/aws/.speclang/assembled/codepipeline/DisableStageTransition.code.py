def handler(store, request: dict) -> dict:
    return store.disable_stage_transition(
        pipeline_name=request["pipelineName"],
        stage_name=request["stageName"],
        transition_type=request["transitionType"],
        reason=request.get("reason"),
    )
