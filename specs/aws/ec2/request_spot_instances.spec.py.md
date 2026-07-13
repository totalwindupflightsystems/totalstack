---
id: "@specs/aws/ec2/request_spot_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RequestSpotInstances"
---

# RequestSpotInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/request_spot_instances
> **spec:implements:** @kind:operation RequestSpotInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RequestSpotInstances.spec.md

Creates a Spot Instance request. For more information, see Work with Spot Instance in the Amazon EC2 User Guide . We strongly discourage using the RequestSpotInstances API because it is a legacy API with no planned investment. For options for requesting Spot Instances, see Which is the best Spot request method to use? in the Amazon EC2 User Guide .

## Input Shape: RequestSpotInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AvailabilityZoneGroup | str |  | The user-specified name for a logical grouping of requests. When you specify an Availability Zone group in a Spot Instan |
| BlockDurationMinutes | int |  | Deprecated. |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceCount | int |  | The maximum number of Spot Instances to launch. Default: 1 |
| InstanceInterruptionBehavior | Any  # complex shape |  | The behavior when a Spot Instance is interrupted. The default is terminate . |
| LaunchGroup | str |  | The instance launch group. Launch groups are Spot Instances that launch together and terminate together. Default: Instan |
| LaunchSpecification | Any  # complex shape |  | The launch specification. |
| SpotPrice | str |  | The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this paramete |
| TagSpecifications | list[Any  # complex shape] |  | The key-value pair for tagging the Spot Instance request on creation. The value for ResourceType must be spot-instances- |
| Type | Any  # complex shape |  | The Spot Instance request type. Default: one-time |
| ValidFrom | Any  # complex shape |  | The start date of the request. If this is a one-time request, the request becomes active at this date and time and remai |
| ValidUntil | Any  # complex shape |  | The end date of the request, in UTC format ( YYYY - MM - DD T HH : MM : SS Z). For a persistent request, the request rem |

## Output Shape: RequestSpotInstancesResult

- **SpotInstanceRequests** (list[Any  # complex shape]): The Spot Instance requests.

## Implementation

```speclang
def request_spot_instances(store, request: dict) -> dict:
    """Creates a Spot Instance request. For more information, see Work with Spot Instance in the Amazon EC2 User Guide . We strongly discourage using the RequestSpotInstances API because it is a legacy API w"""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RequestSpotInstances", request)
```
