---
id: "@specs/aws/ec2/describe_image_usage_report_entries"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeImageUsageReportEntries"
---

# DescribeImageUsageReportEntries

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_image_usage_report_entries
> **spec:implements:** @kind:operation DescribeImageUsageReportEntries
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeImageUsageReportEntries.spec.md

Describes the entries in image usage reports, showing how your images are used across other Amazon Web Services accounts. For more information, see View your AMI usage in the Amazon EC2 User Guide .

## Input Shape: DescribeImageUsageReportEntriesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. account-id - A 12-digit Amazon Web Services account ID. creation-time - The time when the report was create |
| ImageIds | list[Any  # complex shape] |  | The IDs of the images for filtering the report entries. If specified, only report entries containing these images are re |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| ReportIds | list[Any  # complex shape] |  | The IDs of the usage reports. |

## Output Shape: DescribeImageUsageReportEntriesResult

- **ImageUsageReportEntries** (list[Any  # complex shape]): The content of the usage reports.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_image_usage_report_entries(store, request: dict) -> dict:
    """Describes the entries in image usage reports, showing how your images are used across other Amazon Web Services accounts. For more information, see View your AMI usage in the Amazon EC2 User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
