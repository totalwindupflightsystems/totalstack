---
id: "@specs/aws/codeartifact/list_repositories"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on: ["@specs/aws/codeartifact/plan"]
---

# ListRepositories

Returns a list of RepositorySummary objects.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `maxResults` | Integer | No | Max results (1-1000) |
| `nextToken` | PaginationToken | No | Next page token |

## Implementation

```speclang
@dataclass
@kind: operation
def execute_list_repositories(store, request):
    """Returns a list of RepositorySummary objects."""
    max_results = request.get("maxResults", 100)
    next_token = request.get("nextToken")
    repos = sorted(store.repositories.values(), key=lambda r: (r.domain_name, r.name))
    if next_token:
        try: repos = repos[int(next_token):]
        except: pass
    items = repos[:max_results]
    result = {"repositories": [{"name": r.name, "administratorAccount": r.administrator_account, "domainName": r.domain_name, "domainOwner": r.domain_owner, "arn": r.arn, "description": r.description} for r in items]}
    if len(repos) > max_results:
        result["nextToken"] = str(max_results)
    return result
```
