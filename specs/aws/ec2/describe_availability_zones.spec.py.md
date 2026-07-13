---
id: "@specs/aws/ec2/describe_availability_zones"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeAvailabilityZones"
---

# DescribeAvailabilityZones

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_availability_zones
> **spec:implements:** @kind:operation DescribeAvailabilityZones
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeAvailabilityZones.spec.md

Describes the Availability Zones, Local Zones, and Wavelength Zones that are available to you. For more information about Availability Zones, Local Zones, and Wavelength Zones, see Regions and zones in the Amazon EC2 User Guide . The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeAvailabilityZonesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllAvailabilityZones | bool |  | Include all Availability Zones, Local Zones, and Wavelength Zones regardless of your opt-in status. If you do not use th |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. group-long-name - The long name of the zone group for the Availability Zone (for example, US West (Oregon)  |
| ZoneIds | list[str] |  | The IDs of the Availability Zones, Local Zones, and Wavelength Zones. |
| ZoneNames | list[str] |  | The names of the Availability Zones, Local Zones, and Wavelength Zones. |

## Output Shape: DescribeAvailabilityZonesResult

- **AvailabilityZones** (list[Any  # complex shape]): Information about the Availability Zones, Local Zones, and Wavelength Zones.

## Implementation

```speclang
def describe_availability_zones(store, request: dict) -> dict:
    """Describes the Availability Zones, Local Zones, and Wavelength Zones that are available to you. For more information about Availability Zones, Local Zones, and Wavelength Zones, see Regions and zones i"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
