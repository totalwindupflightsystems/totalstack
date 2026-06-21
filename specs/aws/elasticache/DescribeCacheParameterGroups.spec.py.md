---
id: "@specs/aws/elasticache/DescribeCacheParameterGroups"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DescribeCacheParameterGroups

Returns a list of cache parameter group descriptions. If a cache parameter group name is specified, the list contains only the descriptions for that group.

## Input Shape: DescribeCacheParameterGroupsMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheParameterGroupName | String |  |
| MaxRecords | IntegerOptional |  |
| Marker | String |  |

## Output Shape: CacheParameterGroupsMessage
- Marker: String
- CacheParameterGroups: CacheParameterGroupList

## Errors
CacheParameterGroupNotFoundFault, InvalidParameterValueException, InvalidParameterCombinationException

## Implementation

```speclang
def describe_cache_parameter_groups(store, request):
    """Handle DescribeCacheParameterGroups — describe resources."""
    resource_name = request.get("CacheParameterGroupName")
    if resource_name:
        if resource_name not in store.parameter_groups:
            raise CacheParameterGroupNotFoundFault(f"Resource {resource_name} not found")
        return {CacheParameterGroups: [dict(store.parameter_groups[resource_name])]}
    else:
        items = [dict(v) for v in store.parameter_groups.values()]
        return {CacheParameterGroups: items}
```
