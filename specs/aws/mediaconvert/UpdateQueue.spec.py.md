---
id: "@specs/aws/mediaconvert/UpdateQueue"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/mediaconvert/plan"
---

# UpdateQueue

Modify an existing queue.

## Implementation

```speclang
def execute_update_queue(store, request):
    """Update an existing queue."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")
    
    q = store.queues.get(name)
    if not q:
        raise ResourceNotFoundException(f"Queue '{name}' not found")
    
    if 'Description' in request:
        q.description = request['Description']
    if 'Status' in request:
        q.status = request['Status']
    if 'ConcurrentJobs' in request:
        q.concurrent_jobs = request['ConcurrentJobs']
    
    q.last_updated = time.time()
    
    return {"Queue": q.to_dict()}
```
