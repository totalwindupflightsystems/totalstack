def handler(store, r: dict) -> dict:
    return store.describe_groups(r.get("AutoScalingGroupNames"))