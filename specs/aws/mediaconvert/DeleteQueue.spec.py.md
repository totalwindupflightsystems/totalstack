---
id: "@specs/aws/mediaconvert/DeleteQueue"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/mediaconvert/plan"
---

# DeleteQueue

Delete a queue.

## Implementation

```speclang
def execute_delete_queue(store, request):
    """Delete a queue."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")
    
    if name not in store.queues:
        raise ResourceNotFoundException(f"Queue '{name}' not found")
    
    del store.queues[name]
    
    return {}
```
