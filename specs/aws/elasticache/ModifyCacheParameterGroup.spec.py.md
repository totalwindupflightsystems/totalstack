---
id: "@specs/aws/elasticache/ModifyCacheParameterGroup"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# ModifyCacheParameterGroup

Modifies the parameters of a cache parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.

## Input Shape: ModifyCacheParameterGroupMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheParameterGroupName | String | ✓ |
| ParameterNameValues | ParameterNameValueList | ✓ |

## Output Shape: CacheParameterGroupNameMessage
- CacheParameterGroupName: String

## Errors
CacheParameterGroupNotFoundFault, InvalidCacheParameterGroupStateFault, InvalidParameterValueException, InvalidParameterCombinationException, InvalidGlobalReplicationGroupStateFault

## Implementation

```speclang
def modify_cache_parameter_group(store, request):
    """Handle ModifyCacheParameterGroup — modify a resource."""
    resource_name = request.get("CacheParameterGroupName")
    if not resource_name:
        raise InvalidParameterValueException("CacheParameterGroupName is required")
    if resource_name not in store.parameter_groups:
        raise CacheParameterGroupNotFoundFault(f"Resource {resource_name} not found")

    # Update fields from request
    record = store.parameter_groups[resource_name]
    for key, value in request.items():
        if value is not None:
            record[key] = value

    # Build response with updated fields
    response = dict(record)
    response["CacheParameterGroupName"] = resource_name
    return response
```
