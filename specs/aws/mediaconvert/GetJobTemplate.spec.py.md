---
id: "@specs/aws/mediaconvert/GetJobTemplate"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/mediaconvert/plan"
---

# GetJobTemplate

Retrieve a job template by name.

## Implementation

```speclang
def execute_get_job_template(store, request):
    """Get a job template by name."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")
    
    tmpl = store.job_templates.get(name)
    if not tmpl:
        raise ResourceNotFoundException(f"Job template '{name}' not found")
    
    return {"JobTemplate": tmpl.to_dict()}
```
