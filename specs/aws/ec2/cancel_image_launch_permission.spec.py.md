---
id: "@specs/aws/ec2/cancel_image_launch_permission"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CancelImageLaunchPermission"
---

# CancelImageLaunchPermission

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/cancel_image_launch_permission
> **spec:implements:** @kind:operation CancelImageLaunchPermission
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CancelImageLaunchPermission.spec.md

Removes your Amazon Web Services account from the launch permissions for the specified AMI. For more information, see Cancel having an AMI shared with your Amazon Web Services account in the Amazon EC2 User Guide .

## Input Shape: CancelImageLaunchPermissionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI that was shared with your Amazon Web Services account. |

## Output Shape: CancelImageLaunchPermissionResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def cancel_image_launch_permission(store, request: dict) -> dict:
    """Removes your Amazon Web Services account from the launch permissions for the specified AMI. For more information, see Cancel having an AMI shared with your Amazon Web Services account in the Amazon EC"""
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")

    if not store.image_launch_permissions(image_id):
        raise ResourceNotFoundException(f"Resource image_id not found")
    store.delete_image_launch_permissions(image_id)
    return {}
```
