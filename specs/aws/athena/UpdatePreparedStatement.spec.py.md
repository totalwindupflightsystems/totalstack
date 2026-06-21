---
id: "@specs/aws/athena/update-prepared-statement"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/UpdatePreparedStatement.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# UpdatePreparedStatement — Athena

Updates a prepared statement.

## Implementation

```speclang
def update_prepared_statement(store: 'AthenaStore', request: dict) -> dict:
    """Update a prepared statement."""
    name = request.get('StatementName')
    workgroup = request.get('WorkGroup')
    query = request.get('QueryStatement')
    if not name or not workgroup or not query:
        raise InvalidRequestException('StatementName, WorkGroup, and QueryStatement are required')
    key = (workgroup, name)
    if key not in store.prepared_statements:
        raise ResourceNotFoundException(f'Prepared statement {name} not found in workgroup {workgroup}')
    store.prepared_statements[key]['QueryStatement'] = query
    if 'Description' in request:
        store.prepared_statements[key]['Description'] = request['Description']
    return {}
```
