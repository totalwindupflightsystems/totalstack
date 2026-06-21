# spec:trace: aws/mediaconvert/CreateJob.spec.py.md#implementation
# spec:id: @specs/aws/mediaconvert/createjob
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_create_job(store, request):
    """Create a new MediaConvert job."""
    role = request.get('Role')
    settings = request.get('Settings')
    
    if not role:
        raise InvalidParameterException("Role is required")
    if not settings:
        raise InvalidParameterException("Settings is required")
    
    job_id = str(uuid.uuid4()).replace('-', '')[:12]
    
    job = JobRecord(
        id=job_id,
        role=role,
        settings=settings,
        Queue=request.get('Queue', 'Default'),
        JobTemplate=request.get('JobTemplate', ''),
        Priority=request.get('Priority', 0),
        Tags=request.get('Tags', {}),
        UserMetadata=request.get('UserMetadata', {}),
        ClientRequestToken=request.get('ClientRequestToken', ''),
        AccelerationSettings=request.get('AccelerationSettings'),
        StatusUpdateInterval=request.get('StatusUpdateInterval'),
        HopDestinations=request.get('HopDestinations'),
    )
    
    store.jobs[job_id] = job
    
    return {"Job": job.to_dict()}

