---
id: "@specs/aws/athena/create-data-catalog"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/CreateDataCatalog.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# CreateDataCatalog — Athena

Creates a data catalog. Data catalogs are containers for databases and tables.

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Name | String | Yes | Name of the data catalog (1-256 chars) |
| Type | DataCatalogType | Yes | LAMBDA, GLUE, or HIVE |
| Description | String | No | Description of the catalog |
| Parameters | Map | No | Key-value pairs for catalog configuration |
| Tags | TagList | No | Tags |

## Errors

- **InvalidRequestException**: Missing Name/Type or duplicate catalog

## Implementation

```speclang
def create_data_catalog(store: 'AthenaStore', request: dict) -> dict:
    """Create a new Athena data catalog."""
    name = request.get('Name')
    catalog_type = request.get('Type')
    if not name:
        raise InvalidRequestException('Name is required')
    if not catalog_type:
        raise InvalidRequestException('Type is required')
    if name in store.data_catalogs:
        raise InvalidRequestException(f'Data catalog {name} already exists')

    catalog = {
        'Name': name,
        'Type': catalog_type,
        'Description': request.get('Description', ''),
        'Parameters': request.get('Parameters', {}),
    }
    store.data_catalogs[name] = catalog

    # Handle tags
    tags = request.get('Tags', [])
    if tags:
        arn = f'arn:aws:athena:us-east-1:000000000000:datacatalog/{name}'
        store.tags[arn] = {t['Key']: t['Value'] for t in tags}

    return {'DataCatalog': dict(catalog)}
```
