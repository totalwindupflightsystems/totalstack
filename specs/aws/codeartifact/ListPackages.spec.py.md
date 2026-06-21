---
id: "@specs/aws/codeartifact/list_packages"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on: ["@specs/aws/codeartifact/plan"]
---

# ListPackages

Returns a list of PackageSummary objects for packages in a repository.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | DomainName | Yes | Domain name |
| `domainOwner` | AccountId | No | Domain owner account |
| `repository` | RepositoryName | Yes | Repository name |
| `format` | PackageFormat | No | Filter by package format |
| `namespace` | PackageNamespace | No | Filter by namespace |
| `packagePrefix` | PackageName | No | Prefix to filter packages |
| `maxResults` | Integer | No | Max results |
| `nextToken` | PaginationToken | No | Next page token |

## Implementation

```speclang
@dataclass
@kind: operation
def execute_list_packages(store, request):
    """Returns a list of PackageSummary objects for packages in a repository."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not repo_name:
        raise ValidationException("repository is required")
    store._get_repo(domain_name, repo_name)

    key = (domain_name, repo_name)
    pkgs = store.packages.get(key, {})
    items = []
    for pkg_name, info in sorted(pkgs.items()):
        items.append({
            "package": pkg_name,
            "format": info.get("format", "npm"),
            "namespace": info.get("namespace"),
        })
    return {"packages": items}
```
