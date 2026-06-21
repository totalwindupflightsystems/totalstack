---
id: "@specs/aws/codeartifact/list_repos_in_domain"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on: ["@specs/aws/codeartifact/plan"]
---

# ListRepositoriesInDomain

Returns a list of RepositorySummary objects for repositories in a domain.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | DomainName | Yes | Domain name |
| `domainOwner` | AccountId | No | Domain owner account |
| `administratorAccount` | AccountId | No | Filter by admin account |
| `maxResults` | Integer | No | Max results |
| `nextToken` | PaginationToken | No | Next page token |

## Implementation

```speclang
@dataclass
@kind: operation
def execute_list_repositories_in_domain(store, request):
    """Returns a list of RepositorySummary objects for repositories in a domain."""
    domain_name = request.get("domain", "")
    if not domain_name:
        raise ValidationException("domain is required")
    store._get_domain(domain_name)
    admin = request.get("administratorAccount")
    repos = sorted([r for k, r in store.repositories.items() if k[0] == domain_name and (not admin or r.administrator_account == admin)], key=lambda r: r.name)
    max_results = request.get("maxResults", 100)
    items = repos[:max_results]
    result = {"repositories": [{"name": r.name, "administratorAccount": r.administrator_account, "domainName": r.domain_name, "domainOwner": r.domain_owner, "arn": r.arn, "description": r.description} for r in items]}
    if len(repos) > max_results:
        result["nextToken"] = str(max_results)
    return result
```
