---
id: "@specs/aws/ec2/describe_declarative_policies_reports"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeDeclarativePoliciesReports"
---

# DescribeDeclarativePoliciesReports

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_declarative_policies_reports
> **spec:implements:** @kind:operation DescribeDeclarativePoliciesReports
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeDeclarativePoliciesReports.spec.md

Describes the metadata of an account status report, including the status of the report. To view the full report, download it from the Amazon S3 bucket where it was saved. Reports are accessible only when they have the complete status. Reports with other statuses ( running , cancelled , or error ) are not available in the S3 bucket. For more information about downloading objects from an S3 bucket, see Downloading objects in the Amazon Simple Storage Service User Guide . For more information, see Generating the account status report for declarative policies in the Amazon Web Services Organizations User Guide .

## Input Shape: DescribeDeclarativePoliciesReportsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| ReportIds | list[str] |  | One or more report IDs. |

## Output Shape: DescribeDeclarativePoliciesReportsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **Reports** (list[Any  # complex shape]): The report metadata.

## Implementation

```speclang
def describe_declarative_policies_reports(store, request: dict) -> dict:
    """Describes the metadata of an account status report, including the status of the report. To view the full report, download it from the Amazon S3 bucket where it was saved. Reports are accessible only w"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
