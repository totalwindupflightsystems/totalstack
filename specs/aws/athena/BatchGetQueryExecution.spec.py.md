---
id: "@specs/aws/athena/batch-get-query-execution"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/BatchGetQueryExecution.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# BatchGetQueryExecution — Athena

Returns details for multiple query executions.

## Implementation

```speclang
def batch_get_query_execution(store: 'AthenaStore', request: dict) -> dict:
    """Batch get query executions."""
    ids = request.get('QueryExecutionIds', [])
    queries, unprocessed = [], []
    for eid in ids:
        if eid in store.query_executions:
            queries.append(dict(store.query_executions[eid]))
        else:
            unprocessed.append({'QueryExecutionId': eid, 'ErrorCode': 'ResourceNotFound'})
    result = {'QueryExecutions': queries}
    if unprocessed:
        result['UnprocessedQueryExecutionIds'] = unprocessed
    return result
```
