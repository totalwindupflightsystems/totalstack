def handler(store, request: dict) -> dict:
    step = store.describe_step(request["ClusterId"], request["StepId"])
    return {"Step": step.to_dict()}
