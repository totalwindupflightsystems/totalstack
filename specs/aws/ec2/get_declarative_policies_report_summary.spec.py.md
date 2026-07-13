---
id: "@specs/aws/ec2/get_declarative_policies_report_summary"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetDeclarativePoliciesReportSummary"
---

# GetDeclarativePoliciesReportSummary

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_declarative_policies_report_summary
> **spec:implements:** @kind:operation GetDeclarativePoliciesReportSummary
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetDeclarativePoliciesReportSummary.spec.md

Retrieves a summary of the account status report. To view the full report, download it from the Amazon S3 bucket where it was saved. Reports are accessible only when they have the complete status. Reports with other statuses ( running , cancelled , or error ) are not available in the S3 bucket. For more information about downloading objects from an S3 bucket, see Downloading objects in the Amazon Simple Storage Service User Guide . For more information, see Generating the account status report for declarative policies in the Amazon Web Services Organizations User Guide .

## Input Shape: GetDeclarativePoliciesReportSummaryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ReportId | Any  # complex shape | ✓ | The ID of the report. |

## Output Shape: GetDeclarativePoliciesReportSummaryResult

- **AttributeSummaries** (list[Any  # complex shape]): The attributes described in the report.
- **EndTime** (Any  # complex shape): The time when the report generation ended.
- **NumberOfAccounts** (int): The total number of accounts associated with the specified targetId .
- **NumberOfFailedAccounts** (int): The number of accounts where attributes could not be retrieved in any Region.
- **ReportId** (str): The ID of the report.
- **S3Bucket** (str): The name of the Amazon S3 bucket where the report is located.
- **S3Prefix** (str): The prefix for your S3 object.
- **StartTime** (Any  # complex shape): The time when the report generation started.
- **TargetId** (str): The root ID, organizational unit ID, or account ID. Format: For root: r-ab12 For OU: ou-ab12-cdef1234 For account: 12345

## Implementation

```speclang
def get_declarative_policies_report_summary(store, request: dict) -> dict:
    """Retrieves a summary of the account status report. To view the full report, download it from the Amazon S3 bucket where it was saved. Reports are accessible only when they have the complete status. Rep"""
    report_id = request.get("ReportId", "").strip() if isinstance(request.get("ReportId"), str) else request.get("ReportId")
    if not report_id:
        raise ValidationException("ReportId is required")

    resource = store.declarative_policies_report_summarys(report_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource report_id not found")
    return {"ReportId": report_id, **resource}
```
