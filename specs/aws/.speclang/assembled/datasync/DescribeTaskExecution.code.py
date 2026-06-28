def describe_task_execution(store, request: dict) -> dict:
    return store.describe_task_execution(
        TaskExecutionArn=request["TaskExecutionArn"]
    )
