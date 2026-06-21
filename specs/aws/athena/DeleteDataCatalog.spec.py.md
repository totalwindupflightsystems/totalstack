---
id: "@specs/aws/athena/delete-data-catalog"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/DeleteDataCatalog.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# DeleteDataCatalog — Athena

Deletes a data catalog.

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Name | String | Yes | Name of the data catalog |

## Implementation

```speclang
def delete_data_catalog(store: 'AthenaStore', request: dict) -> dict:
    """Delete an Athena data catalog."""
    name = request.get('Name')
    if not name:
        raise InvalidRequestException('Name is required')
    if name not in store.data_catalogs:
        raise ResourceNotFoundException(f'Data catalog {name} not found')
    del store.data_catalogs[name]
    return {}
```
