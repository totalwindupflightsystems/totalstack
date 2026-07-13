---
id: "@specs/aws/cloudformation/describe_resource_scan"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeResourceScan"
---

# DescribeResourceScan

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_resource_scan
> **spec:implements:** @kind:operation DescribeResourceScan
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeResourceScan.spec.md

Describes details of a resource scan.

## Input Shape: DescribeResourceScanInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ResourceScanId | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the resource scan. |

## Output Shape: DescribeResourceScanOutput

- **EndTime** (str  # ISO8601): The time that the resource scan was finished.
- **PercentageCompleted** (Any  # complex shape): The percentage of the resource scan that has been completed.
- **ResourceScanId** (Any  # complex shape): The Amazon Resource Name (ARN) of the resource scan. The format is arn:${Partition}:cloudformation:${Region}:${Account}:
- **ResourceTypes** (Any  # complex shape): The list of resource types for the specified scan. Resource types are only available for scans with a Status set to COMP
- **ResourcesRead** (Any  # complex shape): The number of resources that were read. This is only available for scans with a Status set to COMPLETE , EXPIRED , or FA
- **ResourcesScanned** (Any  # complex shape): The number of resources that were listed. This is only available for scans with a Status set to COMPLETE , EXPIRED , or 
- **ScanFilters** (Any  # complex shape): The scan filters that were used.
- **StartTime** (str  # ISO8601): The time that the resource scan was started.
- **Status** (Any  # complex shape): Status of the resource scan. IN_PROGRESS The resource scan is still in progress. COMPLETE The resource scan is complete.
- **StatusReason** (Any  # complex shape): The reason for the resource scan status, providing more information if a failure happened.

## Errors
- **ResourceScanNotFoundException**: The resource scan was not found.

## Implementation

```speclang
def describe_resource_scan(store, request: dict) -> dict:
    """Describes details of a resource scan."""
    resource_scan_id = request.get("ResourceScanId", "").strip() if isinstance(request.get("ResourceScanId"), str) else request.get("ResourceScanId")
    if not resource_scan_id:
        raise ValidationException("ResourceScanId is required")

    resource = store.resource_scans(resource_scan_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource resource_scan_id not found")
    return {"ResourceScanId": resource_scan_id, **resource}
```
