---
id: "@specs/aws/ec2/describe_network_interface_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeNetworkInterfaceAttribute"
---

# DescribeNetworkInterfaceAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_network_interface_attribute
> **spec:implements:** @kind:operation DescribeNetworkInterfaceAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeNetworkInterfaceAttribute.spec.md

Describes a network interface attribute. You can specify only one attribute at a time.

## Input Shape: DescribeNetworkInterfaceAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape |  | The attribute of the network interface. This parameter is required. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkInterfaceId | Any  # complex shape | ✓ | The ID of the network interface. |

## Output Shape: DescribeNetworkInterfaceAttributeResult

- **AssociatePublicIpAddress** (bool): Indicates whether to assign a public IPv4 address to a network interface. This option can be enabled for any network int
- **Attachment** (Any  # complex shape): The attachment (if any) of the network interface.
- **Description** (Any  # complex shape): The description of the network interface.
- **Groups** (list[Any  # complex shape]): The security groups associated with the network interface.
- **NetworkInterfaceId** (str): The ID of the network interface.
- **SourceDestCheck** (Any  # complex shape): Indicates whether source/destination checking is enabled.

## Implementation

```speclang
def describe_network_interface_attribute(store, request: dict) -> dict:
    """Describes a network interface attribute. You can specify only one attribute at a time."""
    network_interface_id = request.get("NetworkInterfaceId", "").strip() if isinstance(request.get("NetworkInterfaceId"), str) else request.get("NetworkInterfaceId")
    if not network_interface_id:
        raise ValidationException("NetworkInterfaceId is required")

    resource = store.network_interface_attributes(network_interface_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource network_interface_id not found")
    return {"NetworkInterfaceId": network_interface_id, **resource}
```
