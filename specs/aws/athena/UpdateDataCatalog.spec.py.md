---
id: "@specs/aws/athena/update-data-catalog"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/UpdateDataCatalog.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# UpdateDataCatalog — Athena

Updates a data catalog.

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Name | String | Yes | Name of the data catalog |
| Type | DataCatalogType | Yes | Updated type |
| Description | String | No | Updated description |
| Parameters | Map | No | Updated parameters |

## Implementation

```speclang
def update_data_catalog(store: 'AthenaStore', request: dict) -> dict:
    """Update an Athena data catalog."""
    name = request.get('Name')
    catalog_type = request.get('Type')
    if not name:
        raise InvalidRequestException('Name is required')
    if not catalog_type:
        raise InvalidRequestException('Type is required')
    if name not in store.data_catalogs:
        raise ResourceNotFoundException(f'Data catalog {name} not found')

    catalog = store.data_catalogs[name]
    catalog['Type'] = catalog_type
    if 'Description' in request:
        catalog['Description'] = request['Description']
    if 'Parameters' in request:
        catalog['Parameters'] = request['Parameters']

    return {'DataCatalog': dict(catalog)}
```
