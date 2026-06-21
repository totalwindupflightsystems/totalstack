---
id: "@specs/aws/mediaconvert/CancelJob"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/mediaconvert/plan"
---

# CancelJob

Cancel a running job.

## Implementation

```speclang
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
```
