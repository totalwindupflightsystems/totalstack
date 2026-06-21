---
id: "@specs/aws/elasticache/DeleteCacheParameterGroup"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DeleteCacheParameterGroup

Deletes the specified cache parameter group. You cannot delete a cache parameter group if it is associated with any cache clusters. You cannot delete the default cache parameter groups in your account.

## Input Shape: DeleteCacheParameterGroupMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheParameterGroupName | String | ✓ |

## Output Shape: None

## Errors
InvalidCacheParameterGroupStateFault, CacheParameterGroupNotFoundFault, InvalidParameterValueException, InvalidParameterCombinationException

## Implementation

```speclang
def delete_cache_parameter_group(store, request):
    """Handle DeleteCacheParameterGroup — delete a resource."""
    resource_name = request.get("CacheParameterGroupName")
    if not resource_name:
        raise InvalidParameterValueException("CacheParameterGroupName is required")
    if resource_name not in store.parameter_groups:
        raise CacheParameterGroupNotFoundFault(f"Resource {resource_name} not found")
    del store.parameter_groups[resource_name]
    return {}
```
