---
id: "@specs/aws/athena/get-table-metadata"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/GetTableMetadata.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# GetTableMetadata — Athena

Returns table metadata.

## Implementation

```speclang
def get_table_metadata(store: 'AthenaStore', request: dict) -> dict:
    """Get table metadata."""
    catalog = request.get('CatalogName', 'AwsDataCatalog')
    db_name = request.get('DatabaseName')
    table_name = request.get('TableName')
    if not db_name or not table_name:
        raise InvalidRequestException('DatabaseName and TableName are required')
    key = (catalog, db_name, table_name)
    if key not in store.table_metadata:
        raise ResourceNotFoundException(f'Table {table_name} not found in {catalog}.{db_name}')
    return {'TableMetadata': dict(store.table_metadata[key])}
```
