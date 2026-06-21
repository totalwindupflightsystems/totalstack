---
id: "@specs/aws/athena/create-named-query"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/CreateNamedQuery.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# CreateNamedQuery — Athena

Creates a named query in the specified workgroup.

## Implementation

```speclang
def create_named_query(store: 'AthenaStore', request: dict) -> dict:
    """Create a new named query."""
    name = request.get('Name')
    database = request.get('Database')
    query_string = request.get('QueryString')
    workgroup = request.get('WorkGroup', 'primary')
    if not name:
        raise InvalidRequestException('Name is required')
    if not database:
        raise InvalidRequestException('Database is required')
    if not query_string:
        raise InvalidRequestException('QueryString is required')

    import uuid
    query_id = str(uuid.uuid4())
    nq = {
        'Name': name,
        'NamedQueryId': query_id,
        'Database': database,
        'QueryString': query_string,
        'Description': request.get('Description', ''),
        'WorkGroup': workgroup,
    }
    store.named_queries[query_id] = nq
    return {'NamedQueryId': query_id}
```
