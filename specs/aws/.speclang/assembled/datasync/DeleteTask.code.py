def delete_task(store, request: dict) -> dict:
    return store.delete_task(TaskArn=request["TaskArn"])
