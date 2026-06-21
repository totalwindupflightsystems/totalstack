// spec:trace spec=/home/kara/totalstack/specs/aws/athena/BatchGetNamedQuery.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

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