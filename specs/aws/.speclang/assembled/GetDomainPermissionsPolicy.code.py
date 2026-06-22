
def execute_get_domain_permissions_policy(store, request):
    """Returns the resource policy attached to the specified domain."""
    domain_name = request.get("domain", "")
    if not domain_name:
        raise ValidationException("domain is required")
    domain = store._get_domain(domain_name)
    policy = store.domain_policies.get(domain_name, "")
    return {"policy": {"resourceArn": domain.arn, "document": policy, "revision": str(uuid.uuid4().hex[:8])}}
