# spec:trace: aws/codeartifact/DeleteRepository.spec.py.md#implementation
# spec:id: @specs/aws/codeartifact/deleterepository
# spec:generated: DO NOT EDIT — edit the spec instead


def execute_delete_repository(store, request):
    """Deletes a repository."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not repo_name:
        raise ValidationException("repository is required")
    key = (domain_name, repo_name)
    repo = store._get_repo(domain_name, repo_name)
    domain = store._get_domain(domain_name)
    del store.repositories[key]
    store.repo_policies.pop(key, None)
    store.repo_endpoints.pop(key, None)
    store.tags.pop(repo.arn, None)
    domain.repository_count = max(0, domain.repository_count - 1)
    return {"repository": {"name": repo_name, "arn": repo.arn, "status": "Deleted"}}

