---
id: "@specs/aws/mediaconvert/GetQueue"
version: 1.0.0
target_lang: py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/mediaconvert/plan"
---

# GetQueue

Retrieve a queue by name.

## Implementation

```speclang
def execute_get_queue(store, request):
    """Get a queue by name."""
    name = request.get('Name')
    if not name:
        raise InvalidParameterException("Name is required")
    
    q = store.queues.get(name)
    if not q:
        raise ResourceNotFoundException(f"Queue '{name}' not found")
    
    return {"Queue": q.to_dict()}
```
