// spec:trace spec=/home/kara/totalstack/specs/aws/mediaconvert/CancelJob.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def execute_cancel_job(store, request):
    """Cancel a job by ID."""
    job_id = request.get('Id')
    if not job_id:
        raise InvalidParameterException("Id is required")
    
    job = store.jobs.get(job_id)
    if not job:
        raise ResourceNotFoundException(f"Job {job_id} not found")
    
    job.status = "CANCELED"
    
    return {"Job": job.to_dict()}