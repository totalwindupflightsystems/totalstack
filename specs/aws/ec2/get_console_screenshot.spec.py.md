---
id: "@specs/aws/ec2/get_console_screenshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetConsoleScreenshot"
---

# GetConsoleScreenshot

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_console_screenshot
> **spec:implements:** @kind:operation GetConsoleScreenshot
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetConsoleScreenshot.spec.md

Retrieve a JPG-format screenshot of a running instance to help with troubleshooting. The returned content is Base64-encoded. For more information, see Instance console output in the Amazon EC2 User Guide .

## Input Shape: GetConsoleScreenshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |
| WakeUp | bool |  | When set to true , acts as keystroke input and wakes up an instance that's in standby or "sleep" mode. |

## Output Shape: GetConsoleScreenshotResult

- **ImageData** (str): The data that comprises the image.
- **InstanceId** (str): The ID of the instance.

## Implementation

```speclang
def get_console_screenshot(store, request: dict) -> dict:
    """Retrieve a JPG-format screenshot of a running instance to help with troubleshooting. The returned content is Base64-encoded. For more information, see Instance console output in the Amazon EC2 User Gu"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.console_screenshots(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")
    return {"InstanceId": instance_id, **resource}
```
