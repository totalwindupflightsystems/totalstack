---
id: "@specs/aws/elasticache/ModifyCacheSubnetGroup"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# ModifyCacheSubnetGroup

Modifies an existing cache subnet group.

## Input Shape: ModifyCacheSubnetGroupMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheSubnetGroupName | String | ✓ |
| CacheSubnetGroupDescription | String |  |
| SubnetIds | SubnetIdentifierList |  |

## Output Shape: ModifyCacheSubnetGroupResult
- CacheSubnetGroup: CacheSubnetGroup

## Errors
CacheSubnetGroupNotFoundFault, CacheSubnetQuotaExceededFault, SubnetInUse, InvalidSubnet, SubnetNotAllowedFault

## Implementation

```speclang
def modify_cache_subnet_group(store, request):
    """Handle ModifyCacheSubnetGroup — modify a resource."""
    resource_name = request.get("CacheSubnetGroupName")
    if not resource_name:
        raise InvalidParameterValueException("CacheSubnetGroupName is required")
    if resource_name not in store.subnet_groups:
        raise CacheSubnetGroupNotFoundFault(f"Resource {resource_name} not found")

    # Update fields from request
    record = store.subnet_groups[resource_name]
    for key, value in request.items():
        if value is not None:
            record[key] = value

    # Build response with updated fields
    response = dict(record)
    response["CacheSubnetGroupName"] = resource_name
    return response
```
