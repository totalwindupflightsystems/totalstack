// spec:trace spec=/home/kara/totalstack/specs/aws/codeartifact/PutDomainPermissionsPolicy.spec.py.md#input-fields
// spec:generated DO NOT EDIT — edit the spec instead

def execute_put_domain_permissions_policy(store, request):
    """Sets a resource policy on a domain."""
    domain_name = request.get("domain", "")
    policy_doc = request.get("policyDocument", "")
    if not domain_name:
        raise ValidationException("domain is required")
    if not policy_doc:
        raise ValidationException("policyDocument is required")
    domain = store._get_domain(domain_name)
    store.domain_policies[domain_name] = policy_doc
    return {"policy": {"resourceArn": domain.arn, "document": policy_doc, "revision": str(uuid.uuid4().hex[:8])}}