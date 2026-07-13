---
id: "@specs/aws/ec2/describe_image_usage_reports"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeImageUsageReports"
---

# DescribeImageUsageReports

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_image_usage_reports
> **spec:implements:** @kind:operation DescribeImageUsageReports
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeImageUsageReports.spec.md

Describes the configuration and status of image usage reports, filtered by report IDs or image IDs. For more information, see View your AMI usage in the Amazon EC2 User Guide .

## Input Shape: DescribeImageUsageReportsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. creation-time - The time when the report was created, in the ISO 8601 format in the UTC time zone (YYYY-MM- |
| ImageIds | list[Any  # complex shape] |  | The IDs of the images for filtering the reports. If specified, only reports containing these images are returned. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| ReportIds | list[Any  # complex shape] |  | The IDs of the image usage reports. |

## Output Shape: DescribeImageUsageReportsResult

- **ImageUsageReports** (list[Any  # complex shape]): The image usage reports.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_image_usage_reports(store, request: dict) -> dict:
    """Describes the configuration and status of image usage reports, filtered by report IDs or image IDs. For more information, see View your AMI usage in the Amazon EC2 User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
