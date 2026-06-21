---
id: "@specs/aws/athena/get-work-group"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/GetWorkGroup.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# GetWorkGroup — Athena

Returns information about a workgroup.

## Implementation

```speclang
def get_work_group(store: 'AthenaStore', request: dict) -> dict:
    """Get an Athena workgroup by name."""
    name = request.get('WorkGroup')
    if not name:
        raise InvalidRequestException('WorkGroup is required')
    if name not in store.work_groups:
        raise ResourceNotFoundException(f'Workgroup {name} not found')
    return {'WorkGroup': dict(store.work_groups[name])}
```
