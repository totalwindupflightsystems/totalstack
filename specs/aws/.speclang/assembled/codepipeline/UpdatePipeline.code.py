def handler(store, request: dict) -> dict:
    pipeline = request["pipeline"]
    return store.update_pipeline(name=pipeline["name"], pipeline_obj=pipeline)
