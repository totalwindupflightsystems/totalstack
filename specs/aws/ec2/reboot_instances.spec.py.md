---
id: "@specs/aws/ec2/reboot_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RebootInstances"
---

# RebootInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/reboot_instances
> **spec:implements:** @kind:operation RebootInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RebootInstances.spec.md

Requests a reboot of the specified instances. This operation is asynchronous; it only queues a request to reboot the specified instances. The operation succeeds if the instances are valid and belong to you. Requests to reboot terminated instances are ignored. If an instance does not cleanly shut down within a few minutes, Amazon EC2 performs a hard reboot. For more information about troubleshooting, see Troubleshoot an unreachable instance in the Amazon EC2 User Guide .

## Input Shape: RebootInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceIds | list[Any  # complex shape] | ✓ | The instance IDs. |

## Implementation

```speclang
def reboot_instances(store, request: dict) -> dict:
    """Requests a reboot of the specified instances. This operation is asynchronous; it only queues a request to reboot the specified instances. The operation succeeds if the instances are valid and belong t"""
    instance_ids = request.get("InstanceIds", "").strip() if isinstance(request.get("InstanceIds"), str) else request.get("InstanceIds")
    if not instance_ids:
        raise ValidationException("InstanceIds is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RebootInstances", request)
```
