---
id: "@specs/aws/ec2/allocate_hosts"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AllocateHosts"
---

# AllocateHosts

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/allocate_hosts
> **spec:implements:** @kind:operation AllocateHosts
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AllocateHosts.spec.md

Allocates a Dedicated Host to your account. At a minimum, specify the supported instance type or instance family, the Availability Zone in which to allocate the host, and the number of hosts to allocate.

## Input Shape: AllocateHostsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssetIds | list[str] |  | The IDs of the Outpost hardware assets on which to allocate the Dedicated Hosts. Targeting specific hardware assets on a |
| AutoPlacement | Any  # complex shape |  | Indicates whether the host accepts any untargeted instance launches that match its instance type configuration, or if it |
| AvailabilityZone | str |  | The Availability Zone in which to allocate the Dedicated Host. |
| AvailabilityZoneId | Any  # complex shape |  | The ID of the Availability Zone. |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| HostMaintenance | Any  # complex shape |  | Indicates whether to enable or disable host maintenance for the Dedicated Host. For more information, see Host maintenan |
| HostRecovery | Any  # complex shape |  | Indicates whether to enable or disable host recovery for the Dedicated Host. Host recovery is disabled by default. For m |
| InstanceFamily | str |  | Specifies the instance family to be supported by the Dedicated Hosts. If you specify an instance family, the Dedicated H |
| InstanceType | str |  | Specifies the instance type to be supported by the Dedicated Hosts. If you specify an instance type, the Dedicated Hosts |
| OutpostArn | str |  | The Amazon Resource Name (ARN) of the Amazon Web Services Outpost on which to allocate the Dedicated Host. If you specif |
| Quantity | int |  | The number of Dedicated Hosts to allocate to your account with these parameters. If you are allocating the Dedicated Hos |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the Dedicated Host during creation. |

## Output Shape: AllocateHostsResult

- **HostIds** (list[str]): The ID of the allocated Dedicated Host. This is used to launch an instance onto a specific host.

## Implementation

```speclang
def allocate_hosts(store, request: dict) -> dict:
    """Allocates a Dedicated Host to your account. At a minimum, specify the supported instance type or instance family, the Availability Zone in which to allocate the host, and the number of hosts to alloca"""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AllocateHosts", request)
```
