---
id: "@specs/aws/athena/get-query-execution"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/GetQueryExecution.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# GetQueryExecution — Athena

Returns information about a query execution.

## Implementation

```speclang
def get_query_execution(store: 'AthenaStore', request: dict) -> dict:
    """Get a query execution by ID."""
    exec_id = request.get('QueryExecutionId')
    if not exec_id:
        raise InvalidRequestException('QueryExecutionId is required')
    if exec_id not in store.query_executions:
        raise ResourceNotFoundException(f'Query execution {exec_id} not found')
    return {'QueryExecution': dict(store.query_executions[exec_id])}
```
