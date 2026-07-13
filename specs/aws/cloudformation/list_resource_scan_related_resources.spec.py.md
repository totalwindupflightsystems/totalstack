---
id: "@specs/aws/cloudformation/list_resource_scan_related_resources"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListResourceScanRelatedResources"
---

# ListResourceScanRelatedResources

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_resource_scan_related_resources
> **spec:implements:** @kind:operation ListResourceScanRelatedResources
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListResourceScanRelatedResources.spec.md

Lists the related resources for a list of resources from a resource scan. The response indicates whether each returned resource is already managed by CloudFormation.

## Input Shape: ListResourceScanRelatedResourcesInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| MaxResults | Any  # complex shape |  | If the number of available results exceeds this maximum, the response includes a NextToken value that you can use for th |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| ResourceScanId | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the resource scan. |
| Resources | Any  # complex shape | ✓ | The list of resources for which you want to get the related resources. Up to 100 resources can be provided. |

## Output Shape: ListResourceScanRelatedResourcesOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all the remaining results, NextToken is set to a token. To retrieve the next set of result
- **RelatedResources** (Any  # complex shape): List of up to MaxResults resources in the specified resource scan related to the specified resources.

## Errors
- **ResourceScanNotFoundException**: The resource scan was not found.
- **ResourceScanInProgressException**: A resource scan is currently in progress. Only one can be run at a time for an account in a Region.

## Implementation

```speclang
def list_resource_scan_related_resources(store, request: dict) -> dict:
    """Lists the related resources for a list of resources from a resource scan. The response indicates whether each returned resource is already managed by CloudFormation."""
    resource_scan_id = request.get("ResourceScanId", "").strip() if isinstance(request.get("ResourceScanId"), str) else request.get("ResourceScanId")
    if not resource_scan_id:
        raise ValidationException("ResourceScanId is required")
    resources = request.get("Resources", "").strip() if isinstance(request.get("Resources"), str) else request.get("Resources")
    if not resources:
        raise ValidationException("Resources is required")

    items = store.list_resource_scan_related_resourcess()
    return {"RelatedResources": list(items.values())}
```
