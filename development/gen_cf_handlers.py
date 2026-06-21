#!/usr/bin/env python3
"""Write CloudFront handler implementations."""
import os

SERVICE = 'cloudfront'
ASSEMBLED_DIR = f'/home/kara/totalstack/specs/aws/.speclang/assembled/{SERVICE}'
os.makedirs(ASSEMBLED_DIR, exist_ok=True)

handlers = {
    'create-distribution': 'def handler(store, request: dict) -> dict:\n    return store.create_distribution(request.get("CallerReference", "test"), request.get("DistributionConfig", {}))',
    'get-distribution': 'def handler(store, request: dict) -> dict:\n    return store.get_distribution(request["Id"])',
    'get-distribution-config': 'def handler(store, request: dict) -> dict:\n    return store.get_distribution_config(request["Id"])',
    'list-distributions': 'def handler(store, request: dict) -> dict:\n    return store.list_distributions()',
    'update-distribution': 'def handler(store, request: dict) -> dict:\n    return store.update_distribution(request["Id"], request.get("DistributionConfig", {}), request.get("IfMatch", ""))',
    'delete-distribution': 'def handler(store, request: dict) -> dict:\n    return store.delete_distribution(request["Id"])',
    'create-cache-policy': 'def handler(store, request: dict) -> dict:\n    return store.create_cache_policy(request.get("CachePolicyConfig", {}))',
    'get-cache-policy': 'def handler(store, request: dict) -> dict:\n    return store.get_cache_policy(request["Id"])',
    'list-cache-policies': 'def handler(store, request: dict) -> dict:\n    return store.list_cache_policies()',
    'delete-cache-policy': 'def handler(store, request: dict) -> dict:\n    return store.delete_cache_policy(request["Id"])',
    'create-origin-request-policy': 'def handler(store, request: dict) -> dict:\n    return store.create_origin_request_policy(request.get("OriginRequestPolicyConfig", {}))',
    'get-origin-request-policy': 'def handler(store, request: dict) -> dict:\n    return store.get_origin_request_policy(request["Id"])',
    'list-origin-request-policies': 'def handler(store, request: dict) -> dict:\n    return store.list_origin_request_policies()',
    'delete-origin-request-policy': 'def handler(store, request: dict) -> dict:\n    return store.delete_origin_request_policy(request["Id"])',
    'create-response-headers-policy': 'def handler(store, request: dict) -> dict:\n    return store.create_response_headers_policy(request.get("ResponseHeadersPolicyConfig", {}))',
    'get-response-headers-policy': 'def handler(store, request: dict) -> dict:\n    return store.get_response_headers_policy(request["Id"])',
    'list-response-headers-policies': 'def handler(store, request: dict) -> dict:\n    return store.list_response_headers_policies()',
    'delete-response-headers-policy': 'def handler(store, request: dict) -> dict:\n    return store.delete_response_headers_policy(request["Id"])',
    'create-function': 'def handler(store, request: dict) -> dict:\n    return store.create_function(request["Name"], request.get("FunctionCode", b""), request.get("FunctionConfig", {}))',
    'describe-function': 'def handler(store, request: dict) -> dict:\n    return store.describe_function(request["Name"])',
    'list-functions': 'def handler(store, request: dict) -> dict:\n    return store.list_functions()',
    'delete-function': 'def handler(store, request: dict) -> dict:\n    return store.delete_function(request["Name"])',
    'tag-resource': 'def handler(store, request: dict) -> dict:\n    return store.tag_resource(request["ResourceARN"], request["Tags"])',
    'untag-resource': 'def handler(store, request: dict) -> dict:\n    return store.untag_resource(request["ResourceARN"], request["TagKeys"])',
    'list-tags-for-resource': 'def handler(store, request: dict) -> dict:\n    return store.list_tags(request["ResourceARN"])',
}

count = 0
for name, code in handlers.items():
    path = f'{ASSEMBLED_DIR}/{name}.code.py'
    with open(path, 'w') as f:
        f.write(code)
    count += 1

print(f'Wrote {count} handler files to {ASSEMBLED_DIR}/')
