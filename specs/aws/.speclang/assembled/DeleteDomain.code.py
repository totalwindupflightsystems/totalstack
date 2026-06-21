// spec:trace spec=/home/kara/totalstack/specs/aws/codeartifact/DeleteDomain.spec.py.md#input-fields
// spec:generated DO NOT EDIT — edit the spec instead

def execute_delete_domain(store, request):
    """Deletes a domain. You cannot delete a domain that contains repositories."""
    domain_name = request.get("domain", "")
    if not domain_name:
        raise ValidationException("domain is required")

    domain = store._get_domain(domain_name)

    if domain.repository_count > 0:
        raise ConflictException(
            f"Domain {domain_name} contains {domain.repository_count} repositories. Delete them first."
        )

    del store.domains[domain_name]
    store.domain_policies.pop(domain_name, None)
    store.tags.pop(domain.arn, None)

    return {"domain": {"name": domain_name, "arn": domain.arn, "status": "Deleted"}}