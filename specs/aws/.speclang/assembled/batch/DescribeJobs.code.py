def handler(store, request: dict) -> dict:
    return store.describe_jobs(jobs=request["jobs"])
