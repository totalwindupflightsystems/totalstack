def handler(store, request: dict) -> dict:
    return store.delete_compute_environment(
        compute_environment=request["computeEnvironment"],
    )
