---
id: "@specs/aws/codeartifact/list_package_versions"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on: ["@specs/aws/codeartifact/plan"]
---

# ListPackageVersions

Returns a list of PackageVersionSummary objects for package versions in a repository.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | DomainName | Yes | Domain name |
| `domainOwner` | AccountId | No | Domain owner account |
| `repository` | RepositoryName | Yes | Repository name |
| `format` | PackageFormat | Yes | Package format |
| `package` | PackageName | Yes | Package name |
| `namespace` | PackageNamespace | No | Package namespace |
| `status` | PackageVersionStatus | No | Filter by status |
| `sortBy` | PackageVersionSortType | No | Sort order |
| `maxResults` | Integer | No | Max results |
| `nextToken` | PaginationToken | No | Next page token |

## Implementation

```speclang
@dataclass
@kind: operation
def execute_list_package_versions(store, request):
    """Returns a list of PackageVersionSummary objects for package versions in a repository."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    fmt = request.get("format", "")
    package_name = request.get("package", "")
    if not all([domain_name, repo_name, fmt, package_name]):
        raise ValidationException("domain, repository, format, and package are required")
    store._get_repo(domain_name, repo_name)

    key = (domain_name, repo_name, package_name, fmt)
    versions = sorted(store.package_versions.get(key, {}).values(), key=lambda v: v.version, reverse=True)
    status_filter = request.get("status")
    if status_filter:
        versions = [v for v in versions if v.status == status_filter]

    return {
        "versions": [{
            "version": v.version, "revision": v.revision, "status": v.status,
            "format": v.format, "namespace": v.namespace,
        } for v in versions],
        "defaultDisplayVersion": versions[0].version if versions else None,
        "format": fmt, "package": package_name,
    }
```
