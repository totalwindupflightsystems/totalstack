---
id: "@specs/aws/ec2/enable_fast_launch"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableFastLaunch"
---

# EnableFastLaunch

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_fast_launch
> **spec:implements:** @kind:operation EnableFastLaunch
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableFastLaunch.spec.md

When you enable Windows fast launch for a Windows AMI, images are pre-provisioned, using snapshots to launch instances up to 65% faster. To create the optimized Windows image, Amazon EC2 launches an instance and runs through Sysprep steps, rebooting as required. Then it creates a set of reserved snapshots that are used for subsequent launches. The reserved snapshots are automatically replenished as they are used, depending on your settings for launch frequency. You can only change these settings for Windows AMIs that you own or that have been shared with you.

## Input Shape: EnableFastLaunchRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | Specify the ID of the image for which to enable Windows fast launch. |
| LaunchTemplate | Any  # complex shape |  | The launch template to use when launching Windows instances from pre-provisioned snapshots. Launch template parameters c |
| MaxParallelLaunches | int |  | The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Wind |
| ResourceType | str |  | The type of resource to use for pre-provisioning the AMI for Windows fast launch. Supported values include: snapshot , w |
| SnapshotConfiguration | Any  # complex shape |  | Configuration settings for creating and managing the snapshots that are used for pre-provisioning the AMI for Windows fa |

## Output Shape: EnableFastLaunchResult

- **ImageId** (Any  # complex shape): The image ID that identifies the AMI for which Windows fast launch was enabled.
- **LaunchTemplate** (Any  # complex shape): The launch template that is used when launching Windows instances from pre-provisioned snapshots.
- **MaxParallelLaunches** (int): The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Wind
- **OwnerId** (str): The owner ID for the AMI for which Windows fast launch was enabled.
- **ResourceType** (Any  # complex shape): The type of resource that was defined for pre-provisioning the AMI for Windows fast launch.
- **SnapshotConfiguration** (Any  # complex shape): Settings to create and manage the pre-provisioned snapshots that Amazon EC2 uses for faster launches from the Windows AM
- **State** (Any  # complex shape): The current state of Windows fast launch for the specified AMI.
- **StateTransitionReason** (str): The reason that the state changed for Windows fast launch for the AMI.
- **StateTransitionTime** (Any  # complex shape): The time that the state changed for Windows fast launch for the AMI.

## Implementation

```speclang
def enable_fast_launch(store, request: dict) -> dict:
    """When you enable Windows fast launch for a Windows AMI, images are pre-provisioned, using snapshots to launch instances up to 65% faster. To create the optimized Windows image, Amazon EC2 launches an i"""
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    resource = store.enable_fast_launchs(image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_id not found")

    # Update mutable fields
    if "ResourceType" in request:
        resource["ResourceType"] = resource_type
    if "SnapshotConfiguration" in request:
        resource["SnapshotConfiguration"] = snapshot_configuration
    if "LaunchTemplate" in request:
        resource["LaunchTemplate"] = launch_template
    if "MaxParallelLaunches" in request:
        resource["MaxParallelLaunches"] = max_parallel_launches
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_fast_launchs(image_id, resource)
    return resource
```
