---
id: "@specs/aws/ec2/disable_fast_launch"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableFastLaunch"
---

# DisableFastLaunch

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_fast_launch
> **spec:implements:** @kind:operation DisableFastLaunch
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableFastLaunch.spec.md

Discontinue Windows fast launch for a Windows AMI, and clean up existing pre-provisioned snapshots. After you disable Windows fast launch, the AMI uses the standard launch process for each new instance. Amazon EC2 must remove all pre-provisioned snapshots before you can enable Windows fast launch again. You can only change these settings for Windows AMIs that you own or that have been shared with you.

## Input Shape: DisableFastLaunchRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Force | bool |  | Forces the image settings to turn off Windows fast launch for your Windows AMI. This parameter overrides any errors that |
| ImageId | Any  # complex shape | ✓ | Specify the ID of the image for which to disable Windows fast launch. |

## Output Shape: DisableFastLaunchResult

- **ImageId** (Any  # complex shape): The ID of the image for which Windows fast launch was disabled.
- **LaunchTemplate** (Any  # complex shape): The launch template that was used to launch Windows instances from pre-provisioned snapshots.
- **MaxParallelLaunches** (int): The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Wind
- **OwnerId** (str): The owner of the Windows AMI for which Windows fast launch was disabled.
- **ResourceType** (Any  # complex shape): The pre-provisioning resource type that must be cleaned after turning off Windows fast launch for the Windows AMI. Suppo
- **SnapshotConfiguration** (Any  # complex shape): Parameters that were used for Windows fast launch for the Windows AMI before Windows fast launch was disabled. This info
- **State** (Any  # complex shape): The current state of Windows fast launch for the specified Windows AMI.
- **StateTransitionReason** (str): The reason that the state changed for Windows fast launch for the Windows AMI.
- **StateTransitionTime** (Any  # complex shape): The time that the state changed for Windows fast launch for the Windows AMI.

## Implementation

```speclang
def disable_fast_launch(store, request: dict) -> dict:
    """Discontinue Windows fast launch for a Windows AMI, and clean up existing pre-provisioned snapshots. After you disable Windows fast launch, the AMI uses the standard launch process for each new instanc"""
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    resource = store.disable_fast_launchs(image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_id not found")

    # Update mutable fields
    if "Force" in request:
        resource["Force"] = force
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.disable_fast_launchs(image_id, resource)
    return resource
```
