def update_task(store, request: dict) -> dict:
    kw = {k: v for k, v in request.items() if k != "TaskArn"}
    return store.update_task(TaskArn=request["TaskArn"], **kw)
