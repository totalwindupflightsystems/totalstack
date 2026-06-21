---
id: "@specs/aws/athena/batch-get-named-query"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/BatchGetNamedQuery.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# BatchGetNamedQuery — Athena

Returns details for multiple named queries.

## Implementation

```speclang
def batch_get_named_query(store: 'AthenaStore', request: dict) -> dict:
    """Batch get named queries."""
    ids = request.get('NamedQueryIds', [])
    queries, unprocessed = [], []
    for qid in ids:
        if qid in store.named_queries:
            queries.append(dict(store.named_queries[qid]))
        else:
            unprocessed.append({'NamedQueryId': qid, 'ErrorCode': 'ResourceNotFound'})
    result = {'NamedQueries': [{'Name': q['Name'], 'NamedQueryId': q['NamedQueryId'],
             'Database': q['Database'], 'QueryString': q['QueryString'],
             'Description': q.get('Description', ''), 'WorkGroup': q.get('WorkGroup', 'primary')}
             for q in queries]}
    if unprocessed:
        result['UnprocessedNamedQueryIds'] = unprocessed
    return result
```
