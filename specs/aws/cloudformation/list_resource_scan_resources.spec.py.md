---
id: "@specs/aws/cloudformation/list_resource_scan_resources"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListResourceScanResources"
---

# ListResourceScanResources

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_resource_scan_resources
> **spec:implements:** @kind:operation ListResourceScanResources
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListResourceScanResources.spec.md

Lists the resources from a resource scan. The results can be filtered by resource identifier, resource type prefix, tag key, and tag value. Only resources that match all specified filters are returned. The response indicates whether each returned resource is already managed by CloudFormation.

## Input Shape: ListResourceScanResourcesInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| MaxResults | Any  # complex shape |  | If the number of available results exceeds this maximum, the response includes a NextToken value that you can use for th |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| ResourceIdentifier | Any  # complex shape |  | If specified, the returned resources will have the specified resource identifier (or one of them in the case where the r |
| ResourceScanId | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the resource scan. |
| ResourceTypePrefix | Any  # complex shape |  | If specified, the returned resources will be of any of the resource types with the specified prefix. |
| TagKey | Any  # complex shape |  | If specified, the returned resources will have a matching tag key. |
| TagValue | Any  # complex shape |  | If specified, the returned resources will have a matching tag value. |

## Output Shape: ListResourceScanResourcesOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all the remaining results, NextToken is set to a token. To retrieve the next set of result
- **Resources** (Any  # complex shape): List of up to MaxResults resources in the specified resource scan that match all of the specified filters.

## Errors
- **ResourceScanNotFoundException**: The resource scan was not found.
- **ResourceScanInProgressException**: A resource scan is currently in progress. Only one can be run at a time for an account in a Region.

## Implementation

```speclang
def list_resource_scan_resources(store, request: dict) -> dict:
    """Lists the resources from a resource scan. The results can be filtered by resource identifier, resource type prefix, tag key, and tag value. Only resources that match all specified filters are returned"""
    resource_scan_id = request.get("ResourceScanId", "").strip() if isinstance(request.get("ResourceScanId"), str) else request.get("ResourceScanId")
    if not resource_scan_id:
        raise ValidationException("ResourceScanId is required")

    items = store.list_resource_scan_resourcess()
    return {"Resources": list(items.values())}
```
