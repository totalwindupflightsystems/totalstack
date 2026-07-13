---
id: "@specs/aws/ec2/report_instance_status"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ReportInstanceStatus"
---

# ReportInstanceStatus

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/report_instance_status
> **spec:implements:** @kind:operation ReportInstanceStatus
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ReportInstanceStatus.spec.md

Submits feedback about the status of an instance. The instance must be in the running state. If your experience with the instance differs from the instance status returned by DescribeInstanceStatus , use ReportInstanceStatus to report your experience with the instance. Amazon EC2 collects this information to improve the accuracy of status checks. Use of this action does not change the value returned by DescribeInstanceStatus .

## Input Shape: ReportInstanceStatusRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | Any  # complex shape |  | Descriptive text about the health state of your instance. |
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| EndTime | Any  # complex shape |  | The time at which the reported instance health state ended. |
| Instances | list[Any  # complex shape] | ✓ | The instances. |
| ReasonCodes | list[Any  # complex shape] | ✓ | The reason codes that describe the health state of your instance. instance-stuck-in-state : My instance is stuck in a st |
| StartTime | Any  # complex shape |  | The time at which the reported instance health state began. |
| Status | Any  # complex shape | ✓ | The status of all instances listed. |

## Implementation

```speclang
def report_instance_status(store, request: dict) -> dict:
    """Submits feedback about the status of an instance. The instance must be in the running state. If your experience with the instance differs from the instance status returned by DescribeInstanceStatus , """
    instances = request.get("Instances", "").strip() if isinstance(request.get("Instances"), str) else request.get("Instances")
    if not instances:
        raise ValidationException("Instances is required")
    reason_codes = request.get("ReasonCodes", "").strip() if isinstance(request.get("ReasonCodes"), str) else request.get("ReasonCodes")
    if not reason_codes:
        raise ValidationException("ReasonCodes is required")
    status = request.get("Status", "").strip() if isinstance(request.get("Status"), str) else request.get("Status")
    if not status:
        raise ValidationException("Status is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ReportInstanceStatus", request)
```
