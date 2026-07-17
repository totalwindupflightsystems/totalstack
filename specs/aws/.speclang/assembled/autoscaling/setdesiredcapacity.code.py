def handler(store, r: dict) -> dict:
    return store.set_desired_capacity(r["AutoScalingGroupName"], r["DesiredCapacity"])