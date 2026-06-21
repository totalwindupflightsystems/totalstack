---
id: "@specs/aws/athena/delete-work-group"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/DeleteWorkGroup.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# DeleteWorkGroup — Athena

Deletes a workgroup.

## Implementation

```speclang
def delete_work_group(store: 'AthenaStore', request: dict) -> dict:
    """Delete an Athena workgroup."""
    name = request.get('WorkGroup')
    if not name:
        raise InvalidRequestException('WorkGroup is required')
    if name not in store.work_groups:
        raise ResourceNotFoundException(f'Workgroup {name} not found')
    del store.work_groups[name]
    return {}
```
