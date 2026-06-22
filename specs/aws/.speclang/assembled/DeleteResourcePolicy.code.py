
def delete_resource_policy(store, request):
    policy_name = request.get('PolicyName', '')
    if not policy_name:
        raise InvalidRequestException('PolicyName is required')
    policy_revision_id = request.get('PolicyRevisionId', '')
    existing = store.resource_policies.get(policy_name)
    if not existing:
        raise InvalidRequestException(f'Resource policy not found')
    if policy_revision_id and existing.get('PolicyRevisionId') != policy_revision_id:
        raise InvalidPolicyRevisionIdException('Policy revision mismatch')
    del store.resource_policies[policy_name]
    return {}
