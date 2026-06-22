def handler(store, request: dict) -> dict:
    return store.delete_job_queue(job_queue=request["jobQueue"])
