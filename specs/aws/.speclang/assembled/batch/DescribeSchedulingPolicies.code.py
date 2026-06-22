def handler(store, request: dict) -> dict:
    return store.describe_scheduling_policies(arns=request["arns"])
