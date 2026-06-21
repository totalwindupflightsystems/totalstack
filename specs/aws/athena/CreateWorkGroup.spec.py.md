---
id: "@specs/aws/athena/create-work-group"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/CreateWorkGroup.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# CreateWorkGroup — Athena

Creates a workgroup. Workgroups isolate queries and enforce cost controls.

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Name | String | Yes | Workgroup name (1-128 chars) |
| Description | String | No | Description |
| Configuration | WorkGroupConfiguration | No | Configuration (result location, encryption, etc.) |
| Tags | TagList | No | Tags |

## Implementation

```speclang
def create_work_group(store: 'AthenaStore', request: dict) -> dict:
    """Create a new Athena workgroup."""
    name = request.get('Name')
    if not name:
        raise InvalidRequestException('Name is required')
    if name in store.work_groups:
        raise InvalidRequestException(f'Workgroup {name} already exists')

    wg = {
        'Name': name,
        'State': 'ENABLED',
        'Description': request.get('Description', ''),
        'Configuration': request.get('Configuration', {}),
    }
    store.work_groups[name] = wg

    tags = request.get('Tags', [])
    if tags:
        arn = f'arn:aws:athena:us-east-1:000000000000:workgroup/{name}'
        store.tags[arn] = {t['Key']: t['Value'] for t in tags}

    return {'WorkGroup': dict(wg)}
```
