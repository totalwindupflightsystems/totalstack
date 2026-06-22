
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
