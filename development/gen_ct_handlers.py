#!/usr/bin/env python3
"""Write CloudTrail handler implementations."""
import os
ASSEMBLED_DIR = '/home/kara/totalstack/specs/aws/.speclang/assembled/cloudtrail'
os.makedirs(ASSEMBLED_DIR, exist_ok=True)

handlers = {
    'create-trail':     'def handler(store, request: dict) -> dict:\n    return store.create_trail(request["Name"], request["S3BucketName"], IsMultiRegionTrail=request.get("IsMultiRegionTrail", False))',
    'describe-trails':  'def handler(store, request: dict) -> dict:\n    return store.describe_trails(request.get("trailNameList"))',
    'update-trail':     'def handler(store, request: dict) -> dict:\n    kwargs = {k: v for k, v in request.items() if k != "Name" and v is not None}\n    return store.update_trail(request["Name"], **kwargs)',
    'delete-trail':     'def handler(store, request: dict) -> dict:\n    return store.delete_trail(request["Name"])',
    'start-logging':    'def handler(store, request: dict) -> dict:\n    return store.start_logging(request["Name"])',
    'stop-logging':     'def handler(store, request: dict) -> dict:\n    return store.stop_logging(request["Name"])',
    'get-trail-status': 'def handler(store, request: dict) -> dict:\n    return store.get_trail_status(request["Name"])',
    'add-tags':         'def handler(store, request: dict) -> dict:\n    return store.tag_resource(request["ResourceId"], request.get("TagsList", []))',
    'list-tags':        'def handler(store, request: dict) -> dict:\n    return store.list_tags(request["ResourceId"])',
    'remove-tags':      'def handler(store, request: dict) -> dict:\n    return store.remove_tags(request["ResourceId"], request.get("TagsList", []))',
}
count = 0
for name, code in handlers.items():
    with open(f'{ASSEMBLED_DIR}/{name}.code.py', 'w') as f:
        f.write(code)
    count += 1
print(f'{count} handlers')
