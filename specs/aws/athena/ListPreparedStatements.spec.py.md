---
id: "@specs/aws/athena/list-prepared-statements"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/ListPreparedStatements.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# ListPreparedStatements — Athena

Lists prepared statements in a workgroup.

## Implementation

```speclang
def list_prepared_statements(store: 'AthenaStore', request: dict) -> dict:
    """List prepared statements in a workgroup."""
    workgroup = request.get('WorkGroup')
    if not workgroup:
        raise InvalidRequestException('WorkGroup is required')
    max_results = request.get('MaxResults', 50)
    next_token = request.get('NextToken')

    stmts = [dict(v) for (w, _), v in store.prepared_statements.items() if w == workgroup]
    stmts.sort(key=lambda s: s['StatementName'])
    start = int(next_token) if next_token else 0
    page = stmts[start:start + max_results]
    result = {'PreparedStatements': page}
    if start + max_results < len(stmts):
        result['NextToken'] = str(start + max_results)
    return result
```
