---
id: "@specs/aws/ec2/start_declarative_policies_report"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_StartDeclarativePoliciesReport"
---

# StartDeclarativePoliciesReport

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/start_declarative_policies_report
> **spec:implements:** @kind:operation StartDeclarativePoliciesReport
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_StartDeclarativePoliciesReport.spec.md

Generates an account status report. The report is generated asynchronously, and can take several hours to complete. The report provides the current status of all attributes supported by declarative policies for the accounts within the specified scope. The scope is determined by the specified TargetId , which can represent an individual account, or all the accounts that fall under the specified organizational unit (OU) or root (the entire Amazon Web Services Organization). The report is saved to your specified S3 bucket, using the following path structure (with the capitalized placeholders representing your specific values): s3://AMZN-S3-DEMO-BUCKET/YOUR-OPTIONAL-S3-PREFIX/ec2_TARGETID_REPORTID_YYYYMMDDTHHMMZ.csv Prerequisites for generating a report The StartDeclarativePoliciesReport API can only be called by the management account or delegated administrators for the organization. An S3 bucket must be available before generating the report (you can create a new one or use an existing one), it must be in the same Region where the report generation request is made, and it must have an appropriate bucket policy. For a sample S3 policy, see Sample Amazon S3 policy under Examples . Trusted access must be enabled for the service for which the declarative policy will enforce a baseline configuration. If you use the Amazon Web Services Organizations console, this is done automatically when you enable declarative policies. The API uses the following service principal to identify the EC2 service: ec2.amazonaws.com . For more information on how to enable trusted access with the Amazon Web Services CLI and Amazon Web Services SDKs, see Using Organizations with other Amazon Web Services services in the Amazon Web Services Organizations User Guide . Only one report per organization can be generated at a time. Attempting to generate a report while another is in progress will result in an error. For more information, including the required IAM permissions to run this API, see Generating the account status report for declarative policies in the Amazon Web Services Organizations User Guide .

## Input Shape: StartDeclarativePoliciesReportRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| S3Bucket | str | ✓ | The name of the S3 bucket where the report will be saved. The bucket must be in the same Region where the report generat |
| S3Prefix | str |  | The prefix for your S3 object. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply. |
| TargetId | str | ✓ | The root ID, organizational unit ID, or account ID. Format: For root: r-ab12 For OU: ou-ab12-cdef1234 For account: 12345 |

## Output Shape: StartDeclarativePoliciesReportResult

- **ReportId** (str): The ID of the report.

## Implementation

```speclang
def start_declarative_policies_report(store, request: dict) -> dict:
    """Generates an account status report. The report is generated asynchronously, and can take several hours to complete. The report provides the current status of all attributes supported by declarative po"""
    s3_bucket = request.get("S3Bucket", "").strip() if isinstance(request.get("S3Bucket"), str) else request.get("S3Bucket")
    if not s3_bucket:
        raise ValidationException("S3Bucket is required")
    target_id = request.get("TargetId", "").strip() if isinstance(request.get("TargetId"), str) else request.get("TargetId")
    if not target_id:
        raise ValidationException("TargetId is required")

    if store.declarative_policies_reports(target_id):
        raise ResourceInUseException(f"Resource target_id already exists")

    record = {
        "DryRun": dry_run,
        "S3Bucket": s3_bucket,
        "S3Prefix": s3_prefix,
        "TargetId": target_id,
        "TagSpecifications": tag_specifications,
    }

    store.declarative_policies_reports(target_id, record)

    return {
        "ReportId": record.get("ReportId", {}),
    }
```
