---
id: "@specs/aws/elasticache/ListTagsForResource"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# ListTagsForResource

Lists all tags currently on a named resource.  A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track all your ElastiCache resources, with the exception of global replication group. When you add or remove tags on replication groups, those actions will be replicated to all nodes in the replication group. For more information, see Resource-level permissions. If the cluster is not in the available state, ListTagsForResource returns an error.

## Input Shape: ListTagsForResourceMessage
| Parameter | Type | Required |
|-----------|------|----------|
| ResourceName | String | ✓ |

## Output Shape: TagListMessage
- TagList: TagList

## Errors
CacheClusterNotFoundFault, CacheParameterGroupNotFoundFault, CacheSecurityGroupNotFoundFault, CacheSubnetGroupNotFoundFault, InvalidReplicationGroupStateFault, ReplicationGroupNotFoundFault

## Implementation

```speclang
def list_tags_for_resource(store, request):
    """Handle ListTagsForResource."""
    resource_name = request.get("ResourceName")
    if not resource_name:
        raise InvalidParameterValueException("ResourceName is required")
    if resource_name not in store.tags:
        store.tags[resource_name] = []
    return {"TagList": store.tags[resource_name]}
```
