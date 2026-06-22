
def execute_get_job(store, request):
    """Get a job by ID."""
    job_id = request.get('Id')
    if not job_id:
        raise InvalidParameterException("Id is required")

    job = store.jobs.get(job_id)
    if not job:
        raise ResourceNotFoundException(f"Job {job_id} not found")

    return {"Job": job.to_dict()}
