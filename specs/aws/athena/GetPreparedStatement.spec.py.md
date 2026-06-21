---
id: "@specs/aws/athena/get-prepared-statement"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/GetPreparedStatement.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# GetPreparedStatement — Athena

Returns information about a prepared statement.

## Implementation

```speclang
def get_prepared_statement(store: 'AthenaStore', request: dict) -> dict:
    """Get a prepared statement."""
    name = request.get('StatementName')
    workgroup = request.get('WorkGroup')
    if not name:
        raise InvalidRequestException('StatementName is required')
    if not workgroup:
        raise InvalidRequestException('WorkGroup is required')
    key = (workgroup, name)
    if key not in store.prepared_statements:
        raise ResourceNotFoundException(f'Prepared statement {name} not found in workgroup {workgroup}')
    return {'PreparedStatement': dict(store.prepared_statements[key])}
```
