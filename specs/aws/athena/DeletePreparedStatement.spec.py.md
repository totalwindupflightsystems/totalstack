---
id: "@specs/aws/athena/delete-prepared-statement"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/DeletePreparedStatement.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# DeletePreparedStatement — Athena

Deletes a prepared statement.

## Implementation

```speclang
def delete_prepared_statement(store: 'AthenaStore', request: dict) -> dict:
    """Delete a prepared statement."""
    name = request.get('StatementName')
    workgroup = request.get('WorkGroup')
    if not name or not workgroup:
        raise InvalidRequestException('StatementName and WorkGroup are required')
    key = (workgroup, name)
    if key not in store.prepared_statements:
        raise ResourceNotFoundException(f'Prepared statement {name} not found in workgroup {workgroup}')
    del store.prepared_statements[key]
    return {}
```
