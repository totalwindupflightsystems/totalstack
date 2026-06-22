def handler(store, request: dict) -> dict:
    steps = store.list_steps(
        request["ClusterId"],
        StepIds=request.get("StepIds"),
        StepStates=request.get("StepStates"))
    return {"Steps": [s.to_dict() for s in steps]}
