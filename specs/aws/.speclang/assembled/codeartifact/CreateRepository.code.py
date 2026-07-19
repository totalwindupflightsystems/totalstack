# spec:trace: aws/codeartifact/CreateRepository.spec.py.md#implementation
# spec:id: @specs/aws/codeartifact/createrepository
# spec:generated: DO NOT EDIT — edit the spec instead


def execute_create_repository(store, request):
    """Creates a repository."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not repo_name:
        raise ValidationException("repository is required")

    domain = store._get_domain(domain_name)
    _validate_repo_name(repo_name)

    key = (domain_name, repo_name)
    if key in store.repositories:
        raise ConflictException(f"Repository {repo_name} already exists in domain {domain_name}")

    repo = RepositoryRecord(
        name=repo_name,
        domain_name=domain_name,
        domain_owner=domain.owner,
        description=request.get("description"),
    )
    if request.get("upstreams"):
        repo.upstreams = request["upstreams"]

    store.repositories[key] = repo
    store.repo_policies[key] = ""
    store.repo_endpoints[key] = {
        "npm": f"https://{domain_name}-{repo_name}.d.codeartifact.us-east-1.amazonaws.com/npm/",
        "pypi": f"https://{domain_name}-{repo_name}.d.codeartifact.us-east-1.amazonaws.com/pypi/",
        "maven": f"https://{domain_name}-{repo_name}.d.codeartifact.us-east-1.amazonaws.com/maven/",
    }
    domain.repository_count += 1

    result = {
        "repository": {
            "name": repo.name,
            "administratorAccount": repo.administrator_account,
            "domainName": repo.domain_name,
            "domainOwner": repo.domain_owner,
            "arn": repo.arn,
            "description": repo.description,
            "upstreams": repo.upstreams,
            "externalConnections": repo.external_connections,
            "createdTime": repo.created_time,
        }
    }

    if request.get("tags"):
        for tag in request["tags"]:
            store.tags[repo.arn][tag["key"]] = tag["value"]

    return result

