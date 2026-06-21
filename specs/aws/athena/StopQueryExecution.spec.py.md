---
id: "@specs/aws/athena/stop-query-execution"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/StopQueryExecution.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# StopQueryExecution — Athena

Stops a running query execution.

## Implementation

```speclang
def stop_query_execution(store: 'AthenaStore', request: dict) -> dict:
    """Stop a query execution."""
    exec_id = request.get('QueryExecutionId')
    if not exec_id:
        raise InvalidRequestException('QueryExecutionId is required')
    if exec_id not in store.query_executions:
        raise ResourceNotFoundException(f'Query execution {exec_id} not found')
    qe = store.query_executions[exec_id]
    import time
    qe['Status'] = {'State': 'CANCELLED', 'SubmissionDateTime': qe['Status'].get('SubmissionDateTime', time.time()),
                     'CompletionDateTime': time.time()}
    return {}
```
