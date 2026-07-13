---
id: "@specs/aws/ec2/describe_capacity_manager_data_exports"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCapacityManagerDataExports"
---

# DescribeCapacityManagerDataExports

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_capacity_manager_data_exports
> **spec:implements:** @kind:operation DescribeCapacityManagerDataExports
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCapacityManagerDataExports.spec.md

Describes one or more Capacity Manager data export configurations. Returns information about export settings, delivery status, and recent export activity.

## Input Shape: DescribeCapacityManagerDataExportsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityManagerDataExportIds | Any  # complex shape |  | The IDs of the data export configurations to describe. If not specified, all export configurations are returned. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters to narrow the results. Supported filters include export status, creation date, and S3 bucket name. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in a single call. If not specified, up to 1000 results are returned. |
| NextToken | str |  | The token for the next page of results. Use this value in a subsequent call to retrieve additional results. |

## Output Shape: DescribeCapacityManagerDataExportsResult

- **CapacityManagerDataExports** (Any  # complex shape): Information about the data export configurations, including export settings, delivery status, and recent activity.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_capacity_manager_data_exports(store, request: dict) -> dict:
    """Describes one or more Capacity Manager data export configurations. Returns information about export settings, delivery status, and recent export activity."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
