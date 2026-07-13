---
id: "@specs/aws/ec2/create_image_usage_report"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateImageUsageReport"
---

# CreateImageUsageReport

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_image_usage_report
> **spec:implements:** @kind:operation CreateImageUsageReport
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateImageUsageReport.spec.md

Creates a report that shows how your image is used across other Amazon Web Services accounts. The report provides visibility into which accounts are using the specified image, and how many resources (EC2 instances or launch templates) are referencing it. For more information, see View your AMI usage in the Amazon EC2 User Guide .

## Input Shape: CreateImageUsageReportRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AccountIds | list[str] |  | The Amazon Web Services account IDs to include in the report. To include all accounts, omit this parameter. |
| ClientToken | str |  | A unique, case-sensitive identifier that you provide to ensure idempotency of the request. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the image to report on. |
| ResourceTypes | list[Any  # complex shape] | ✓ | The resource types to include in the report. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the report on creation. The ResourceType must be set to image-usage-report ; any other value will c |

## Output Shape: CreateImageUsageReportResult

- **ReportId** (Any  # complex shape): The ID of the report.

## Implementation

```speclang
def create_image_usage_report(store, request: dict) -> dict:
    """Creates a report that shows how your image is used across other Amazon Web Services accounts. The report provides visibility into which accounts are using the specified image, and how many resources ("""
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")
    resource_types = request.get("ResourceTypes", "").strip() if isinstance(request.get("ResourceTypes"), str) else request.get("ResourceTypes")
    if not resource_types:
        raise ValidationException("ResourceTypes is required")

    if store.image_usage_reports(image_id):
        raise ResourceInUseException(f"Resource image_id already exists")

    record = {
        "ImageId": image_id,
        "DryRun": dry_run,
        "ResourceTypes": resource_types,
        "AccountIds": account_ids,
        "ClientToken": client_token,
        "TagSpecifications": tag_specifications,
    }

    store.image_usage_reports(image_id, record)

    return {
        "ReportId": record.get("ReportId", {}),
    }
```
