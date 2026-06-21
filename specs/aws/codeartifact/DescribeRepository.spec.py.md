---
id: "@specs/aws/codeartifact/describe_repository"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on: ["@specs/aws/codeartifact/plan"]
---

# DescribeRepository

Returns a RepositoryDescription object for the requested repository.

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
def execute_describe_repository(store, request):
    """Returns a RepositoryDescription object for the requested repository."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not repo_name:
        raise ValidationException("repository is required")
    repo = store._get_repo(domain_name, repo_name)
    return {
        "repository": {
            "name": repo.name, "administratorAccount": repo.administrator_account,
            "domainName": repo.domain_name, "domainOwner": repo.domain_owner,
            "arn": repo.arn, "description": repo.description,
            "upstreams": repo.upstreams, "externalConnections": repo.external_connections,
            "createdTime": repo.created_time,
        }
    }
```
