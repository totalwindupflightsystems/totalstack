// spec:trace spec=/home/kara/totalstack/specs/aws/mediaconvert/CreateJobTemplate.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def execute_create_job_template(store, request):
    """Create a new job template."""
    name = request.get('Name')
    settings = request.get('Settings')
    
    if not name:
        raise InvalidParameterException("Name is required")
    if not settings:
        raise InvalidParameterException("Settings is required")
    
    if name in store.job_templates:
        raise ConflictException(f"Job template '{name}' already exists")
    
    tmpl = JobTemplateRecord(
        name=name,
        settings=settings,
        Description=request.get('Description', ''),
        Category=request.get('Category', ''),
        Queue=request.get('Queue', ''),
        Priority=request.get('Priority', 0),
        Tags=request.get('Tags', {}),
        AccelerationSettings=request.get('AccelerationSettings'),
        StatusUpdateInterval=request.get('StatusUpdateInterval'),
    )
    
    store.job_templates[name] = tmpl
    
    return {"JobTemplate": tmpl.to_dict()}