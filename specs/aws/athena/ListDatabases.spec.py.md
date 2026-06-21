---
id: "@specs/aws/athena/list-databases"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/ListDatabases.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# ListDatabases — Athena

Lists databases in a data catalog.

## Implementation

```speclang
def list_databases(store: 'AthenaStore', request: dict) -> dict:
    """List databases in a catalog."""
    catalog = request.get('CatalogName', 'AwsDataCatalog')
    max_results = request.get('MaxResults', 50)
    next_token = request.get('NextToken')

    dbs = sorted([dict(v) for (c, _), v in store.databases.items() if c == catalog],
                 key=lambda d: d.get('Name', ''))
    start = int(next_token) if next_token else 0
    page = dbs[start:start + max_results]
    result = {'DatabaseList': page}
    if start + max_results < len(dbs):
        result['NextToken'] = str(start + max_results)
    return result
```
