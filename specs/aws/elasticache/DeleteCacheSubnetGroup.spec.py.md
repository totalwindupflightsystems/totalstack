---
id: "@specs/aws/elasticache/DeleteCacheSubnetGroup"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DeleteCacheSubnetGroup

Deletes a cache subnet group.  You cannot delete a default cache subnet group or one that is associated with any clusters.

## Input Shape: DeleteCacheSubnetGroupMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheSubnetGroupName | String | ✓ |

## Output Shape: None

## Errors
CacheSubnetGroupInUse, CacheSubnetGroupNotFoundFault

## Implementation

```speclang
def delete_cache_subnet_group(store, request):
    """Handle DeleteCacheSubnetGroup — delete a resource."""
    resource_name = request.get("CacheSubnetGroupName")
    if not resource_name:
        raise InvalidParameterValueException("CacheSubnetGroupName is required")
    if resource_name not in store.subnet_groups:
        raise CacheSubnetGroupNotFoundFault(f"Resource {resource_name} not found")
    del store.subnet_groups[resource_name]
    return {}
```
