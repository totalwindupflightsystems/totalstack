---
id: "@specs/aws/athena/update-work-group"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/UpdateWorkGroup.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# UpdateWorkGroup — Athena

Updates a workgroup configuration.

## Implementation

```speclang
def update_work_group(store: 'AthenaStore', request: dict) -> dict:
    """Update an Athena workgroup."""
    name = request.get('WorkGroup')
    if not name:
        raise InvalidRequestException('WorkGroup is required')
    if name not in store.work_groups:
        raise ResourceNotFoundException(f'Workgroup {name} not found')
    wg = store.work_groups[name]
    if 'Description' in request:
        wg['Description'] = request['Description']
    if 'ConfigurationUpdates' in request:
        wg['Configuration'].update(request['ConfigurationUpdates'])
    if 'State' in request:
        wg['State'] = request['State']
    return {'WorkGroup': dict(wg)}
```
