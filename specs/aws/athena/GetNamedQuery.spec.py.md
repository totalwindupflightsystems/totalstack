---
id: "@specs/aws/athena/get-named-query"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/GetNamedQuery.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# GetNamedQuery — Athena

Returns information about a named query.

## Implementation

```speclang
def get_named_query(store: 'AthenaStore', request: dict) -> dict:
    """Get a named query by ID."""
    query_id = request.get('NamedQueryId')
    if not query_id:
        raise InvalidRequestException('NamedQueryId is required')
    if query_id not in store.named_queries:
        raise ResourceNotFoundException(f'Named query {query_id} not found')
    return {'NamedQuery': dict(store.named_queries[query_id])}
```
