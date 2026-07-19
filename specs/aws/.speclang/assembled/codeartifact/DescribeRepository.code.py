# spec:trace: aws/codeartifact/DescribeRepository.spec.py.md#implementation
# spec:id: @specs/aws/codeartifact/describerepository
# spec:generated: DO NOT EDIT — edit the spec instead


def execute_describe_repository(store, request):
    """Returns a RepositoryDescription object for the requested repository."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not repo_name:
        raise ValidationException("repository is required")
    repo = store._get_repo(domain_name, repo_name)
    return {
        "repository": {
            "name": repo.name, "administratorAccount": repo.administrator_account,
            "domainName": repo.domain_name, "domainOwner": repo.domain_owner,
            "arn": repo.arn, "description": repo.description,
            "upstreams": repo.upstreams, "externalConnections": repo.external_connections,
            "createdTime": repo.created_time,
        }
    }

