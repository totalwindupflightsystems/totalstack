---
id: "@specs/aws/cloudformation/start_resource_scan"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_StartResourceScan"
---

# StartResourceScan

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/start_resource_scan
> **spec:implements:** @kind:operation StartResourceScan
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_StartResourceScan.spec.md

Starts a scan of the resources in this account in this Region. You can the status of a scan using the ListResourceScans API action.

## Input Shape: StartResourceScanInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientRequestToken | Any  # complex shape |  | A unique identifier for this StartResourceScan request. Specify this token if you plan to retry requests so that CloudFo |
| ScanFilters | Any  # complex shape |  | The scan filters to use. |

## Output Shape: StartResourceScanOutput

- **ResourceScanId** (Any  # complex shape): The Amazon Resource Name (ARN) of the resource scan. The format is arn:${Partition}:cloudformation:${Region}:${Account}:

## Errors
- **ResourceScanInProgressException**: A resource scan is currently in progress. Only one can be run at a time for an account in a Region.
- **ResourceScanLimitExceededException**: The limit on resource scans has been exceeded. Reasons include: Exceeded the daily quota for resource scans. A resource scan recently failed. You must wait 10 minutes before starting a new resource sc

## Implementation

```speclang
def start_resource_scan(store, request: dict) -> dict:
    """Starts a scan of the resources in this account in this Region. You can the status of a scan using the ListResourceScans API action."""


    record = {
        "ClientRequestToken": client_request_token,
        "ScanFilters": scan_filters,
    }

    store.resource_scans(record)

    return {
        "ResourceScanId": record.get("ResourceScanId", {}),
    }
```
