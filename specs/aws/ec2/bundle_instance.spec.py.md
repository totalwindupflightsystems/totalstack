---
id: "@specs/aws/ec2/bundle_instance"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_BundleInstance"
---

# BundleInstance

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/bundle_instance
> **spec:implements:** @kind:operation BundleInstance
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_BundleInstance.spec.md

Bundles an Amazon instance store-backed Windows instance. During bundling, only the root device volume (C:\) is bundled. Data on other instance store volumes is not preserved. This action is not applicable for Linux/Unix instances or Windows instances that are backed by Amazon EBS.

## Input Shape: BundleInstanceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance to bundle. Default: None |
| Storage | Any  # complex shape | ✓ | The bucket in which to store the AMI. You can specify a bucket that you already own or a new bucket that Amazon EC2 crea |

## Output Shape: BundleInstanceResult

- **BundleTask** (Any  # complex shape): Information about the bundle task.

## Implementation

```speclang
def bundle_instance(store, request: dict) -> dict:
    """Bundles an Amazon instance store-backed Windows instance. During bundling, only the root device volume (C:\) is bundled. Data on other instance store volumes is not preserved. This action is not appli"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")
    storage = request.get("Storage", "").strip() if isinstance(request.get("Storage"), str) else request.get("Storage")
    if not storage:
        raise ValidationException("Storage is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("BundleInstance", request)
```
