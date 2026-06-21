// spec:trace spec=/home/kara/totalstack/specs/aws/mediaconvert/DeleteJobTemplate.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def execute_delete_job_template(store, request):
    """Delete a job template."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")
    
    if name not in store.job_templates:
        raise ResourceNotFoundException(f"Job template '{name}' not found")
    
    del store.job_templates[name]
    
    return {}