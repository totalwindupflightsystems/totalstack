
def execute_delete_domain_permissions_policy(store, request):
    """Deletes the resource policy set on a domain."""
    domain_name = request.get("domain", "")
    if not domain_name:
        raise ValidationException("domain is required")
    domain = store._get_domain(domain_name)
    store.domain_policies[domain_name] = ""
    return {"policy": {"resourceArn": domain.arn, "document": "", "revision": str(uuid.uuid4().hex[:8])}}
