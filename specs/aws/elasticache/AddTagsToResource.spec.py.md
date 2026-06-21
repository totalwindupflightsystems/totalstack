---
id: "@specs/aws/elasticache/AddTagsToResource"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# AddTagsToResource

A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track all your ElastiCache resources, with the exception of global replication group. When you add or remove tags on replication groups, those actions will be replicated to all nodes in the replication group. For more information, see Resource-level permissions.  For example, you can use cost-allocation tags to your ElastiCache resources, Amazon generates a cost allocation report as a comma-s

## Input Shape: AddTagsToResourceMessage
| Parameter | Type | Required |
|-----------|------|----------|
| ResourceName | String | ✓ |
| Tags | TagList | ✓ |

## Output Shape: TagListMessage
- TagList: TagList

## Errors
CacheClusterNotFoundFault, CacheParameterGroupNotFoundFault, CacheSecurityGroupNotFoundFault, CacheSubnetGroupNotFoundFault, InvalidReplicationGroupStateFault, ReplicationGroupNotFoundFault

## Implementation

```speclang
def add_tags_to_resource(store, request):
    """Handle AddTagsToResource."""
    resource_name = request.get("ResourceName")
    if not resource_name:
        raise InvalidParameterValueException("ResourceName is required")
    if resource_name not in store.tags:
        store.tags[resource_name] = []
    tags = request.get("Tags", [])
    if not tags:
        raise InvalidParameterValueException("Tags is required")
    for tag in tags:
        store.tags[resource_name].append(tag)
    return {}
```
