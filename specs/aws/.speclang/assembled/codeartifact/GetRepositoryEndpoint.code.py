# spec:trace: aws/codeartifact/GetRepositoryEndpoint.spec.py.md#implementation
# spec:id: @specs/aws/codeartifact/getrepositoryendpoint
# spec:generated: DO NOT EDIT — edit the spec instead

@dataclass
def execute_get_repository_endpoint(store, request):
    """Returns the endpoint of a repository for a specific package format."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    fmt = request.get("format", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not repo_name:
        raise ValidationException("repository is required")
    if not fmt:
        raise ValidationException("format is required")
    repo = store._get_repo(domain_name, repo_name)
    key = (domain_name, repo_name)
    endpoints = store.repo_endpoints.get(key, {})
    endpoint = endpoints.get(fmt, f"https://{domain_name}-{repo_name}.d.codeartifact.us-east-1.amazonaws.com/{fmt}/")
    return {"repositoryEndpoint": endpoint}

