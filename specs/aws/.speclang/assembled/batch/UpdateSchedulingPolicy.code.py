def handler(store, request: dict) -> dict:
    return store.update_scheduling_policy(
        arn=request["arn"],
        fairshare_policy=request.get("fairsharePolicy"),
    )
