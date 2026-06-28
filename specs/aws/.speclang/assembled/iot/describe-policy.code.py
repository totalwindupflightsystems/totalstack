def describe_policy(store, request: dict) -> dict:
    return store.describe_policy(request["policyName"])
