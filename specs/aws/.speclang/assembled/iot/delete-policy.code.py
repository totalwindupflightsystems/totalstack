def delete_policy(store, request: dict) -> dict:
    store.delete_policy(request["policyName"])
    return {}
