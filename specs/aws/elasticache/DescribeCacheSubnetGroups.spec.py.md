---
id: "@specs/aws/elasticache/DescribeCacheSubnetGroups"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DescribeCacheSubnetGroups

Returns a list of cache subnet group descriptions. If a subnet group name is specified, the list contains only the description of that group. This is applicable only when you have ElastiCache in VPC setup. All ElastiCache clusters now launch in VPC by default.

## Input Shape: DescribeCacheSubnetGroupsMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheSubnetGroupName | String |  |
| MaxRecords | IntegerOptional |  |
| Marker | String |  |

## Output Shape: CacheSubnetGroupMessage
- Marker: String
- CacheSubnetGroups: CacheSubnetGroups

## Errors
CacheSubnetGroupNotFoundFault

## Implementation

```speclang
def describe_cache_subnet_groups(store, request):
    """Handle DescribeCacheSubnetGroups — describe resources."""
    resource_name = request.get("CacheSubnetGroupName")
    if resource_name:
        if resource_name not in store.subnet_groups:
            raise CacheSubnetGroupNotFoundFault(f"Resource {resource_name} not found")
        return {CacheSubnetGroups: [dict(store.subnet_groups[resource_name])]}
    else:
        items = [dict(v) for v in store.subnet_groups.values()]
        return {CacheSubnetGroups: items}
```
