def handler(store, r: dict) -> dict:
    return store.delete_group(r["AutoScalingGroupName"], r.get("ForceDelete", False))