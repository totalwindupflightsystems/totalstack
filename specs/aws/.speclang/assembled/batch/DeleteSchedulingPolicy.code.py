def handler(store, request: dict) -> dict:
    return store.delete_scheduling_policy(arn=request["arn"])
