// spec:trace spec=/home/kara/totalstack/specs/aws/codeartifact/ListPackageVersions.spec.py.md#input-fields
// spec:generated DO NOT EDIT — edit the spec instead

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