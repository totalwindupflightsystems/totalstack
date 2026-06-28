def describe_task(store, request: dict) -> dict:
    return store.describe_task(TaskArn=request["TaskArn"])
