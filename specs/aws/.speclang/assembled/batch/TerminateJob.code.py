def handler(store, request: dict) -> dict:
    return store.terminate_job(
        job_id=request["jobId"],
        reason=request["reason"],
    )
