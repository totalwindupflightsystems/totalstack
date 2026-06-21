---
id: "@specs/aws/codeartifact/get_pkg_version_readme"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on: ["@specs/aws/codeartifact/plan"]
---

# GetPackageVersionReadme

Gets the readme file for a package version.

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
def execute_get_package_version_readme(store, request):
    """Gets the readme file for a package version."""
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
        raise ResourceNotFoundException(f"Package version {version} not found")
    return {
        "format": fmt, "package": package_name, "version": version,
        "readme": f"# {package_name} v{version}\n\nA sample package for testing.",
    }
```
