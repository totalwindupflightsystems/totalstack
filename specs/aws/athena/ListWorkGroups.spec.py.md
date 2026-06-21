---
id: "@specs/aws/athena/list-work-groups"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/ListWorkGroups.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# ListWorkGroups — Athena

Lists all workgroups.

## Implementation

```speclang
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
```
