---
id: "@specs/aws/elasticache/RemoveTagsFromResource"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# RemoveTagsFromResource

Removes the tags identified by the TagKeys list from the named resource. A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track all your ElastiCache resources, with the exception of global replication group. When you add or remove tags on replication groups, those actions will be replicated to all nodes in the replication group. For more information, see Resource-level permissions.

## Input Shape: RemoveTagsFromResourceMessage
| Parameter | Type | Required |
|-----------|------|----------|
| ResourceName | String | ✓ |
| TagKeys | KeyList | ✓ |

## Output Shape: TagListMessage
- TagList: TagList

## Errors
CacheClusterNotFoundFault, CacheParameterGroupNotFoundFault, CacheSecurityGroupNotFoundFault, CacheSubnetGroupNotFoundFault, InvalidReplicationGroupStateFault, ReplicationGroupNotFoundFault

## Implementation

```speclang
def remove_tags_from_resource(store, request):
    """Handle RemoveTagsFromResource."""
    resource_name = request.get("ResourceName")
    if not resource_name:
        raise InvalidParameterValueException("ResourceName is required")
    if resource_name not in store.tags:
        store.tags[resource_name] = []
    tag_keys = request.get("TagKeys", [])
    if not tag_keys:
        raise InvalidParameterValueException("TagKeys is required")
    store.tags[resource_name] = [
        t for t in store.tags[resource_name]
        if t.get("Key") not in tag_keys
    ]
    return {}
```
