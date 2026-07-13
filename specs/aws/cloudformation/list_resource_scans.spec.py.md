---
id: "@specs/aws/cloudformation/list_resource_scans"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListResourceScans"
---

# ListResourceScans

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_resource_scans
> **spec:implements:** @kind:operation ListResourceScans
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListResourceScans.spec.md

List the resource scans from newest to oldest. By default it will return up to 10 resource scans.

## Input Shape: ListResourceScansInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| MaxResults | Any  # complex shape |  | If the number of available results exceeds this maximum, the response includes a NextToken value that you can use for th |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| ScanTypeFilter | Any  # complex shape |  | The scan type that you want to get summary information about. The default is FULL . |

## Output Shape: ListResourceScansOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all the remaining results, NextToken is set to a token. To retrieve the next set of result
- **ResourceScanSummaries** (Any  # complex shape): The list of scans returned.

## Implementation

```speclang
def list_resource_scans(store, request: dict) -> dict:
    """List the resource scans from newest to oldest. By default it will return up to 10 resource scans."""

    items = store.list_resource_scanss()
    return {"ResourceScanSummaries": list(items.values())}
```
