---
id: "@specs/aws/elasticache/CreateCacheParameterGroup"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# CreateCacheParameterGroup

Creates a new Amazon ElastiCache cache parameter group. An ElastiCache cache parameter group is a collection of parameters and their values that are applied to all of the nodes in any cluster or replication group using the CacheParameterGroup. A newly created CacheParameterGroup is an exact duplicate of the default parameter group for the CacheParameterGroupFamily. To customize the newly created CacheParameterGroup you can change the values of specific parameters. For more information, see:    M

## Input Shape: CreateCacheParameterGroupMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheParameterGroupName | String | ✓ |
| CacheParameterGroupFamily | String | ✓ |
| Description | String | ✓ |
| Tags | TagList |  |

## Output Shape: CreateCacheParameterGroupResult
- CacheParameterGroup: CacheParameterGroup

## Errors
CacheParameterGroupQuotaExceededFault, CacheParameterGroupAlreadyExistsFault, InvalidCacheParameterGroupStateFault, TagQuotaPerResourceExceeded, InvalidParameterValueException, InvalidParameterCombinationException

## Implementation

```speclang
def create_cache_parameter_group(store, request):
    """Handle CreateCacheParameterGroup — create a new resource."""
    if "CacheParameterGroupName" not in request or not request["CacheParameterGroupName"]:
        raise InvalidParameterValueException("CacheParameterGroupName is required")
    if "CacheParameterGroupFamily" not in request or not request["CacheParameterGroupFamily"]:
        raise InvalidParameterValueException("CacheParameterGroupFamily is required")
    if "Description" not in request or not request["Description"]:
        raise InvalidParameterValueException("Description is required")
    resource_name = request["CacheParameterGroupName"]
    if resource_name in store.parameter_groups:
        raise CacheParameterGroupAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"

    store.parameter_groups[resource_name] = record

    # Build response
    response = {}
    response["CacheParameterGroupName"] = resource_name
    response["Status"] = "available"
    return response
```
