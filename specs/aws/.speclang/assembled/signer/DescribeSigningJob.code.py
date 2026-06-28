def handler(store, request):
    jobId = request["jobId"]
    job = store.jobs(jobId)
    if not job:
        raise ResourceNotFoundException(f"Signing job {jobId} not found")
    return job.to_dict()
