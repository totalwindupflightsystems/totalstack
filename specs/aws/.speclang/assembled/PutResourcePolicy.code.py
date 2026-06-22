
def put_resource_policy(store, request):
    policy_name = request.get('PolicyName', '')
    policy_doc = request.get('PolicyDocument', '')
    if not policy_name or not policy_doc:
        raise InvalidRequestException('PolicyName and PolicyDocument are required')
    policy_revision_id = request.get('PolicyRevisionId', '')
    import json
    try:
        json.loads(policy_doc)
    except json.JSONDecodeError:
        raise MalformedPolicyDocumentException('Invalid policy document JSON')
    existing = store.resource_policies.get(policy_name)
    import uuid
    new_revision = str(uuid.uuid4())
    if existing and policy_revision_id:
        if existing.get('PolicyRevisionId') != policy_revision_id:
            raise InvalidPolicyRevisionIdException('Policy revision mismatch')
    store.resource_policies[policy_name] = {
        'PolicyName': policy_name,
        'PolicyDocument': json.dumps(json.loads(policy_doc)),
        'PolicyRevisionId': new_revision,
        'LastUpdatedTime': '2024-01-01T00:00:00Z',
    }
    result = {'ResourcePolicy': store.resource_policies[policy_name]}
    if existing and not policy_revision_id:
        result['ResourcePolicy']['PolicyRevisionId'] = existing['PolicyRevisionId']
    return result
