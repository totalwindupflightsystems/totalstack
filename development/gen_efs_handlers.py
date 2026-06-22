#!/usr/bin/env python3
import os
d = '/home/kara/totalstack/specs/aws/.speclang/assembled/efs'
os.makedirs(d, exist_ok=True)
for name, code in {
    'createfilesystem': "store.create_filesystem(r.get('CreationToken', 'test'))",
    'describefilesystems': "store.describe_filesystems(r.get('FileSystemId'), r.get('CreationToken'))",
    'deletefilesystem': "store.delete_filesystem(r['FileSystemId'])",
    'createmounttarget': "store.create_mount_target(r['FileSystemId'], r['SubnetId'])",
    'describemounttargets': "store.describe_mount_targets(r.get('FileSystemId'), r.get('MountTargetId'))",
    'deletemounttarget': "store.delete_mount_target(r['MountTargetId'])",
    'tagresource': "store.tag_resource(r['ResourceId'], r['Tags'])",
    'listtagsforresource': "store.list_tags(r['ResourceId'])",
    'untagresource': "store.untag_resource(r['ResourceId'], r['TagKeys'])",
}.items():
    with open(f'{d}/{name}.code.py', 'w') as f:
        f.write(f'def handler(store, r: dict) -> dict:\n    return {code}')
print('9 handlers')
