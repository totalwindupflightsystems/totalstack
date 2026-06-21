---
id: "@specs/aws/athena/get-data-catalog"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/GetDataCatalog.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# GetDataCatalog — Athena

Returns the specified data catalog.

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Name | String | Yes | Name of the data catalog |

## Errors
- **InvalidRequestException**: Missing Name
- **ResourceNotFoundException**: Catalog not found

## Implementation

```speclang
def get_data_catalog(store: 'AthenaStore', request: dict) -> dict:
    """Get an Athena data catalog by name."""
    name = request.get('Name')
    if not name:
        raise InvalidRequestException('Name is required')
    if name not in store.data_catalogs:
        raise ResourceNotFoundException(f'Data catalog {name} not found')
    return {'DataCatalog': dict(store.data_catalogs[name])}
```
