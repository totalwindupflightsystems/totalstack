#!/usr/bin/env python3
import os
d = '/home/kara/totalstack/specs/aws/.speclang/assembled/ecr'
os.makedirs(d, exist_ok=True)
for name, code in {
    'create-repository': 'def handler(store, r: dict) -> dict:\n    return store.create_repository(r["repositoryName"])',
    'describe-repositories': 'def handler(store, r: dict) -> dict:\n    return store.describe_repositories(r.get("repositoryNames"))',
    'delete-repository': 'def handler(store, r: dict) -> dict:\n    return store.delete_repository(r["repositoryName"], r.get("force", False))',
    'put-image': 'def handler(store, r: dict) -> dict:\n    return store.put_image(r["repositoryName"], r["imageManifest"], r.get("imageTag"))',
    'describe-images': 'def handler(store, r: dict) -> dict:\n    return store.describe_images(r["repositoryName"])',
    'tag-resource': 'def handler(store, r: dict) -> dict:\n    return store.tag_resource(r["resourceArn"], r["tags"])',
    'list-tags': 'def handler(store, r: dict) -> dict:\n    return store.list_tags(r["resourceArn"])',
    'untag-resource': 'def handler(store, r: dict) -> dict:\n    return store.untag_resource(r["resourceArn"], r["tagKeys"])',
}.items():
    with open(f'{d}/{name}.code.py', 'w') as f: f.write(code)
print(f'8 handlers → {d}/')
