---
id: "@specs/aws/ec2/cancel_declarative_policies_report"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CancelDeclarativePoliciesReport"
---

# CancelDeclarativePoliciesReport

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/cancel_declarative_policies_report
> **spec:implements:** @kind:operation CancelDeclarativePoliciesReport
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CancelDeclarativePoliciesReport.spec.md

Cancels the generation of an account status report. You can only cancel a report while it has the running status. Reports with other statuses ( complete , cancelled , or error ) can't be canceled. For more information, see Generating the account status report for declarative policies in the Amazon Web Services Organizations User Guide .

## Input Shape: CancelDeclarativePoliciesReportRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ReportId | Any  # complex shape | ✓ | The ID of the report. |

## Output Shape: CancelDeclarativePoliciesReportResult

- **Return** (bool): Is true if the request succeeds, and an error otherwise.

## Implementation

```speclang
def cancel_declarative_policies_report(store, request: dict) -> dict:
    """Cancels the generation of an account status report. You can only cancel a report while it has the running status. Reports with other statuses ( complete , cancelled , or error ) can't be canceled. For"""
    report_id = request.get("ReportId", "").strip() if isinstance(request.get("ReportId"), str) else request.get("ReportId")

    if not store.declarative_policies_reports(report_id):
        raise ResourceNotFoundException(f"Resource report_id not found")
    store.delete_declarative_policies_reports(report_id)
    return {}
```
