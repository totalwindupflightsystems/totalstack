---
id: "@specs/aws/mediaconvert/GetJob"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/mediaconvert/plan"
---

# GetJob

Retrieve a job by ID.

## Implementation

```speclang
def execute_get_job(store, request):
    """Get a job by ID."""
    job_id = request.get('Id')
    if not job_id:
        raise InvalidParameterException("Id is required")
    
    job = store.jobs.get(job_id)
    if not job:
        raise ResourceNotFoundException(f"Job {job_id} not found")
    
    return {"Job": job.to_dict()}
```
