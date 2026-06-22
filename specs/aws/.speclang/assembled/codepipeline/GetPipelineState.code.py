def handler(store, request: dict) -> dict:
    return store.get_pipeline_state(name=request["name"])
