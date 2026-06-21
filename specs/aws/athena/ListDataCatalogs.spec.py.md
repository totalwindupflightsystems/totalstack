---
id: "@specs/aws/athena/list-data-catalogs"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/ListDataCatalogs.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# ListDataCatalogs — Athena

Lists all data catalogs.

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| MaxResults | Integer | No | Max results (default 50) |
| NextToken | String | No | Pagination token |

## Implementation

```speclang
def list_data_catalogs(store: 'AthenaStore', request: dict) -> dict:
    """List all Athena data catalogs."""
    max_results = request.get('MaxResults', 50)
    next_token = request.get('NextToken')

    catalog_names = sorted(store.data_catalogs.keys())
    start_idx = int(next_token) if next_token else 0
    page = catalog_names[start_idx:start_idx + max_results]

    catalogs = [dict(store.data_catalogs[n]) for n in page]
    result = {'DataCatalogsSummary': [
        {'CatalogName': c['Name'], 'Type': c['Type']} for c in catalogs
    ]}

    if start_idx + max_results < len(catalog_names):
        result['NextToken'] = str(start_idx + max_results)
    return result
```
