---
id: "@specs/aws/ec2/delete_image_usage_report"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteImageUsageReport"
---

# DeleteImageUsageReport

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_image_usage_report
> **spec:implements:** @kind:operation DeleteImageUsageReport
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteImageUsageReport.spec.md

Deletes the specified image usage report. For more information, see View your AMI usage in the Amazon EC2 User Guide .

## Input Shape: DeleteImageUsageReportRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ReportId | Any  # complex shape | ✓ | The ID of the report to delete. |

## Output Shape: DeleteImageUsageReportResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def delete_image_usage_report(store, request: dict) -> dict:
    """Deletes the specified image usage report. For more information, see View your AMI usage in the Amazon EC2 User Guide ."""
    report_id = request.get("ReportId", "").strip() if isinstance(request.get("ReportId"), str) else request.get("ReportId")

    if not store.image_usage_reports(report_id):
        raise ResourceNotFoundException(f"Resource report_id not found")
    store.delete_image_usage_reports(report_id)
    return {}
```
