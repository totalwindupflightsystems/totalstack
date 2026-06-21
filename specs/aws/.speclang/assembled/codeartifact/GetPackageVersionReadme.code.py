# spec:trace: aws/codeartifact/GetPackageVersionReadme.spec.py.md#implementation
# spec:id: @specs/aws/codeartifact/getpackageversionreadme
# spec:generated: DO NOT EDIT — edit the spec instead

@dataclass
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

