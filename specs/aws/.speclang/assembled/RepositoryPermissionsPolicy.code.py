
def execute_get_repository_permissions_policy(store, request):
    """Returns the resource policy attached to a repository."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not repo_name:
        raise ValidationException("repository is required")
    repo = store._get_repo(domain_name, repo_name)
    key = (domain_name, repo_name)
    policy = store.repo_policies.get(key, "")
    return {"policy": {"resourceArn": repo.arn, "document": policy, "revision": str(uuid.uuid4().hex[:8])}}

def execute_put_repository_permissions_policy(store, request):
    """Sets a resource policy on a repository."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    policy_doc = request.get("policyDocument", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not repo_name:
        raise ValidationException("repository is required")
    if not policy_doc:
        raise ValidationException("policyDocument is required")
    repo = store._get_repo(domain_name, repo_name)
    key = (domain_name, repo_name)
    store.repo_policies[key] = policy_doc
    return {"policy": {"resourceArn": repo.arn, "document": policy_doc, "revision": str(uuid.uuid4().hex[:8])}}

def execute_delete_repository_permissions_policy(store, request):
    """Deletes the resource policy on a repository."""
    domain_name = request.get("domain", "")
    repo_name = request.get("repository", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not repo_name:
        raise ValidationException("repository is required")
    repo = store._get_repo(domain_name, repo_name)
    key = (domain_name, repo_name)
    store.repo_policies[key] = ""
    return {"policy": {"resourceArn": repo.arn, "document": "", "revision": str(uuid.uuid4().hex[:8])}}
