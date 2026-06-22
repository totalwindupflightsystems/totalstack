def handler(store, request: dict) -> dict:
    return store.deregister_job_definition(
        job_definition=request["jobDefinition"],
    )
