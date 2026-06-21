# spec:trace: aws/mediaconvert/GetJobTemplate.spec.py.md#implementation
# spec:id: @specs/aws/mediaconvert/getjobtemplate
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_get_job_template(store, request):
    """Get a job template by name."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")
    
    tmpl = store.job_templates.get(name)
    if not tmpl:
        raise ResourceNotFoundException(f"Job template '{name}' not found")
    
    return {"JobTemplate": tmpl.to_dict()}

