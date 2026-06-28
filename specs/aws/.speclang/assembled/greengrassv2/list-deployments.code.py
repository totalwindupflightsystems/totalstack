def list_deployments(store, request: dict) -> dict:
    deps = store.list_deployments()
    return {"deployments": deps}
