---
id: "@specs/aws/athena/get-database"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/GetDatabase.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# GetDatabase — Athena

Returns a database object.

## Implementation

```speclang
def get_database(store: 'AthenaStore', request: dict) -> dict:
    """Get a database from a catalog."""
    catalog = request.get('CatalogName', 'AwsDataCatalog')
    db_name = request.get('DatabaseName')
    if not db_name:
        raise InvalidRequestException('DatabaseName is required')
    key = (catalog, db_name)
    if key not in store.databases:
        raise ResourceNotFoundException(f'Database {db_name} not found in catalog {catalog}')
    return {'Database': dict(store.databases[key])}
```
