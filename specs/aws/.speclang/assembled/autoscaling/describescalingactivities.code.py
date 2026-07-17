def handler(store, r: dict) -> dict:
    return store.describe_activities(r.get("AutoScalingGroupName"))