#!/usr/bin/env python3
"""Write Cognito Identity handlers."""
import os
d = '/home/kara/totalstack/specs/aws/.speclang/assembled/cognito-identity'
os.makedirs(d, exist_ok=True)
for name, code in {
    'create-identity-pool': 'def handler(store, request: dict) -> dict:\n    return store.create_identity_pool(request["IdentityPoolName"], request.get("AllowUnauthenticatedIdentities", False))',
    'describe-identity-pool': 'def handler(store, request: dict) -> dict:\n    return store.describe_identity_pool(request["IdentityPoolId"])',
    'list-identity-pools': 'def handler(store, request: dict) -> dict:\n    return store.list_identity_pools(request.get("MaxResults", 60))',
    'update-identity-pool': 'def handler(store, request: dict) -> dict:\n    kwargs = {k: v for k, v in request.items() if k != "IdentityPoolId" and v is not None}\n    return store.update_identity_pool(request["IdentityPoolId"], **kwargs)',
    'delete-identity-pool': 'def handler(store, request: dict) -> dict:\n    return store.delete_identity_pool(request["IdentityPoolId"])',
    'get-id': 'def handler(store, request: dict) -> dict:\n    return store.get_id(request["IdentityPoolId"], request.get("Logins"))',
    'get-credentials': 'def handler(store, request: dict) -> dict:\n    return store.get_credentials_for_identity(request["IdentityId"])',
    'tag-resource': 'def handler(store, request: dict) -> dict:\n    return store.tag_resource(request["ResourceArn"], request.get("Tags", {}))',
    'list-tags': 'def handler(store, request: dict) -> dict:\n    return store.list_tags(request["ResourceArn"])',
    'untag-resource': 'def handler(store, request: dict) -> dict:\n    return store.untag_resource(request["ResourceArn"], request.get("TagKeys", []))',
}.items():
    with open(f'{d}/{name}.code.py', 'w') as f: f.write(code)
print(f'10 handlers → {d}/')
