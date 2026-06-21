---
id: "@specs/aws/athena/update-named-query"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/UpdateNamedQuery.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# UpdateNamedQuery — Athena

Updates a named query.

## Implementation

```speclang
def update_named_query(store: 'AthenaStore', request: dict) -> dict:
    """Update a named query."""
    query_id = request.get('NamedQueryId')
    if not query_id:
        raise InvalidRequestException('NamedQueryId is required')
    if query_id not in store.named_queries:
        raise ResourceNotFoundException(f'Named query {query_id} not found')
    nq = store.named_queries[query_id]
    if 'Name' in request:
        nq['Name'] = request['Name']
    if 'Description' in request:
        nq['Description'] = request['Description']
    if 'QueryString' in request:
        nq['QueryString'] = request['QueryString']
    return {}
```
