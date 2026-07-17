def handler(store, r: dict) -> dict:
    kwargs = {k: v for k, v in r.items() if k != "AutoScalingGroupName" and v is not None}
    return store.update_group(r["AutoScalingGroupName"], **kwargs)