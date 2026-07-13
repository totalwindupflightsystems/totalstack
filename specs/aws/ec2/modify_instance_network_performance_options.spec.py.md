---
id: "@specs/aws/ec2/modify_instance_network_performance_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyInstanceNetworkPerformanceOptions"
---

# ModifyInstanceNetworkPerformanceOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_instance_network_performance_options
> **spec:implements:** @kind:operation ModifyInstanceNetworkPerformanceOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyInstanceNetworkPerformanceOptions.spec.md

Change the configuration of the network performance options for an existing instance.

## Input Shape: ModifyInstanceNetworkPerformanceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| BandwidthWeighting | Any  # complex shape | ✓ | Specify the bandwidth weighting option to boost the associated type of baseline bandwidth, as follows: default This opti |
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance to update. |

## Output Shape: ModifyInstanceNetworkPerformanceResult

- **BandwidthWeighting** (Any  # complex shape): Contains the updated configuration for bandwidth weighting on the specified instance.
- **InstanceId** (Any  # complex shape): The instance ID that was updated.

## Implementation

```speclang
def modify_instance_network_performance_options(store, request: dict) -> dict:
    """Change the configuration of the network performance options for an existing instance."""
    bandwidth_weighting = request.get("BandwidthWeighting", "").strip() if isinstance(request.get("BandwidthWeighting"), str) else request.get("BandwidthWeighting")
    if not bandwidth_weighting:
        raise ValidationException("BandwidthWeighting is required")
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.instance_network_performance_optionss(bandwidth_weighting)
    if not resource:
        raise ResourceNotFoundException(f"Resource bandwidth_weighting not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.instance_network_performance_optionss(bandwidth_weighting, resource)
    return resource
```
