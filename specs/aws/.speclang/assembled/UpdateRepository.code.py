
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
