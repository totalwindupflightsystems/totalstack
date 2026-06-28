def list_policies(store, request: dict) -> dict:
    policies = store.list_policies()
    return {"policies": policies}
