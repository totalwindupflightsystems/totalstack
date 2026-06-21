---
id: "@specs/aws/codeartifact/describe_pkg_version"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on: ["@specs/aws/codeartifact/plan"]
---

# DescribePackageVersion

Returns a PackageVersionDescription object for a package version.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | DomainName | Yes | Domain name |
| `domainOwner` | AccountId | No | Domain owner account |
| `repository` | RepositoryName | Yes | Repository name |
| `format` | PackageFormat | Yes | Package format |
| `package` | PackageName | Yes | Package name |
| `packageVersion` | PackageVersion | Yes | Version string |
| `namespace` | PackageNamespace | No | Namespace |

## Implementation

```speclang
@dataclass
@kind: operation
def execute_describe_package_version(store, request):
    """Returns a PackageVersionDescription object for a package version."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    fmt = request.get("format", "")
    package_name = request.get("package", "")
    version = request.get("packageVersion", "")
    if not all([domain_name, repo_name, fmt, package_name, version]):
        raise ValidationException("domain, repository, format, package, and packageVersion are required")
    store._get_repo(domain_name, repo_name)
    key = (domain_name, repo_name, package_name, fmt)
    versions = store.package_versions.get(key, {})
    if version not in versions:
        raise ResourceNotFoundException(f"Package version {version} not found for {package_name}")
    v = versions[version]
    return {
        "packageVersion": {
            "version": v.version, "revision": v.revision, "status": v.status,
            "format": v.format, "namespace": v.namespace,
            "packageName": v.package_name, "publishedTime": v.published_time,
        },
        "format": fmt, "package": package_name, "version": version,
    }
```
