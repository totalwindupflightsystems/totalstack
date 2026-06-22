def handler(store, request: dict) -> dict:
    return store.cancel_job(
        job_id=request["jobId"],
        reason=request["reason"],
    )
