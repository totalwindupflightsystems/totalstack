---
id: "@specs/aws/codeartifact/update_repository"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on: ["@specs/aws/codeartifact/plan"]
---

# UpdateRepository

Update the properties of a repository.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | DomainName | Yes | Domain name |
| `domainOwner` | AccountId | No | Domain owner account |
| `repository` | RepositoryName | Yes | Repository name |
| `description` | Description | No | Updated description |
| `upstreams` | UpstreamRepositoryList | No | Updated upstreams |

## Implementation

```speclang
@dataclass
@kind: operation
def execute_update_repository(store, request):
    """Update the properties of a repository."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not repo_name:
        raise ValidationException("repository is required")
    repo = store._get_repo(domain_name, repo_name)
    if "description" in request:
        repo.description = request["description"]
    if "upstreams" in request:
        repo.upstreams = request["upstreams"]
    return {
        "repository": {
            "name": repo.name, "administratorAccount": repo.administrator_account,
            "domainName": repo.domain_name, "domainOwner": repo.domain_owner,
            "arn": repo.arn, "description": repo.description,
            "upstreams": repo.upstreams, "externalConnections": repo.external_connections,
        }
    }
```
