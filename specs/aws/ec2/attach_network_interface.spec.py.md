---
id: "@specs/aws/ec2/attach_network_interface"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AttachNetworkInterface"
---

# AttachNetworkInterface

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/attach_network_interface
> **spec:implements:** @kind:operation AttachNetworkInterface
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AttachNetworkInterface.spec.md

Attaches a network interface to an instance.

## Input Shape: AttachNetworkInterfaceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DeviceIndex | int | ✓ | The index of the device for the network interface attachment. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EnaQueueCount | int |  | The number of ENA queues to be created with the instance. |
| EnaSrdSpecification | Any  # complex shape |  | Configures ENA Express for the network interface that this action attaches to the instance. |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |
| NetworkCardIndex | int |  | The index of the network card. Some instance types support multiple network cards. The primary network interface must be |
| NetworkInterfaceId | Any  # complex shape | ✓ | The ID of the network interface. |

## Output Shape: AttachNetworkInterfaceResult

- **AttachmentId** (str): The ID of the network interface attachment.
- **NetworkCardIndex** (int): The index of the network card.

## Implementation

```speclang
def attach_network_interface(store, request: dict) -> dict:
    """Attaches a network interface to an instance."""
    device_index = request.get("DeviceIndex", "").strip() if isinstance(request.get("DeviceIndex"), str) else request.get("DeviceIndex")
    if not device_index:
        raise ValidationException("DeviceIndex is required")
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")
    network_interface_id = request.get("NetworkInterfaceId", "").strip() if isinstance(request.get("NetworkInterfaceId"), str) else request.get("NetworkInterfaceId")
    if not network_interface_id:
        raise ValidationException("NetworkInterfaceId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachNetworkInterface", request)
```
