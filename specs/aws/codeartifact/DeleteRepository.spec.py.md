---
id: "@specs/aws/codeartifact/delete_repository"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on: ["@specs/aws/codeartifact/plan"]
---

# DeleteRepository

Deletes a repository.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | DomainName | Yes | Domain name |
| `domainOwner` | AccountId | No | Domain owner account |
| `repository` | RepositoryName | Yes | Repository name |

## Implementation

```speclang
@dataclass
@kind: operation
def execute_delete_repository(store, request):
    """Deletes a repository."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not repo_name:
        raise ValidationException("repository is required")
    key = (domain_name, repo_name)
    repo = store._get_repo(domain_name, repo_name)
    domain = store._get_domain(domain_name)
    del store.repositories[key]
    store.repo_policies.pop(key, None)
    store.repo_endpoints.pop(key, None)
    store.tags.pop(repo.arn, None)
    domain.repository_count = max(0, domain.repository_count - 1)
    return {"repository": {"name": repo_name, "arn": repo.arn, "status": "Deleted"}}
```
