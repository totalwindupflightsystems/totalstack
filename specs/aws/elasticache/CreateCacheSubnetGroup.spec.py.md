---
id: "@specs/aws/elasticache/CreateCacheSubnetGroup"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# CreateCacheSubnetGroup

Creates a new cache subnet group. Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).

## Input Shape: CreateCacheSubnetGroupMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheSubnetGroupName | String | ✓ |
| CacheSubnetGroupDescription | String | ✓ |
| SubnetIds | SubnetIdentifierList | ✓ |
| Tags | TagList |  |

## Output Shape: CreateCacheSubnetGroupResult
- CacheSubnetGroup: CacheSubnetGroup

## Errors
CacheSubnetGroupAlreadyExistsFault, CacheSubnetGroupQuotaExceededFault, CacheSubnetQuotaExceededFault, TagQuotaPerResourceExceeded, InvalidSubnet, SubnetNotAllowedFault

## Implementation

```speclang
def create_cache_subnet_group(store, request):
    """Handle CreateCacheSubnetGroup — create a new resource."""
    if "CacheSubnetGroupName" not in request or not request["CacheSubnetGroupName"]:
        raise InvalidParameterValueException("CacheSubnetGroupName is required")
    if "CacheSubnetGroupDescription" not in request or not request["CacheSubnetGroupDescription"]:
        raise InvalidParameterValueException("CacheSubnetGroupDescription is required")
    if "SubnetIds" not in request or not request["SubnetIds"]:
        raise InvalidParameterValueException("SubnetIds is required")
    resource_name = request["CacheSubnetGroupName"]
    if resource_name in store.subnet_groups:
        raise CacheSubnetGroupAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"

    store.subnet_groups[resource_name] = record

    # Build response
    response = {}
    response["CacheSubnetGroupName"] = resource_name
    response["Status"] = "available"
    return response
```
