---
id: "@specs/aws/mediaconvert/CreateJobTemplate"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/mediaconvert/plan"
---

# CreateJobTemplate

Create a new job template with transcoding settings.

## Implementation

```speclang
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
```
