# spec:trace: aws/athena/ListWorkGroups.spec.py.md#implementation
# spec:id: @specs/aws/athena/listworkgroups
# spec:generated: DO NOT EDIT — edit the spec instead

def list_work_groups(store: 'AthenaStore', request: dict) -> dict:
    """List all Athena workgroups."""
    max_results = request.get('MaxResults', 50)
    next_token = request.get('NextToken')
    names = sorted(store.work_groups.keys())
    start = int(next_token) if next_token else 0
    page = names[start:start + max_results]
    result = {'WorkGroups': [
        {'Name': n, 'State': store.work_groups[n]['State'],
         'Description': store.work_groups[n]['Description']}
        for n in page
    ]}
    if start + max_results < len(names):
        result['NextToken'] = str(start + max_results)
    return result

