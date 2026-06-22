def handler(store, request: dict) -> dict:
    return store.create_scheduling_policy(
        name=request["name"],
        fairshare_policy=request.get("fairsharePolicy"),
        tags=request.get("tags"),
    )
