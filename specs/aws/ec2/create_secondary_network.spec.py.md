---
id: "@specs/aws/ec2/create_secondary_network"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateSecondaryNetwork"
---

# CreateSecondaryNetwork

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_secondary_network
> **spec:implements:** @kind:operation CreateSecondaryNetwork
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateSecondaryNetwork.spec.md

Creates a secondary network. The allowed size for a secondary network CIDR block is between /28 netmask (16 IP addresses) and /12 netmask (1,048,576 IP addresses).

## Input Shape: CreateSecondaryNetworkRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Ipv4CidrBlock | str | ✓ | The IPv4 CIDR block for the secondary network. The CIDR block size must be between /12 and /28. |
| NetworkType | Any  # complex shape | ✓ | The type of secondary network. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the secondary network. |

## Output Shape: CreateSecondaryNetworkResult

- **ClientToken** (str): Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided
- **SecondaryNetwork** (Any  # complex shape): Information about the secondary network.

## Implementation

```speclang
def create_secondary_network(store, request: dict) -> dict:
    """Creates a secondary network. The allowed size for a secondary network CIDR block is between /28 netmask (16 IP addresses) and /12 netmask (1,048,576 IP addresses)."""
    ipv4_cidr_block = request.get("Ipv4CidrBlock", "").strip() if isinstance(request.get("Ipv4CidrBlock"), str) else request.get("Ipv4CidrBlock")
    if not ipv4_cidr_block:
        raise ValidationException("Ipv4CidrBlock is required")
    network_type = request.get("NetworkType", "").strip() if isinstance(request.get("NetworkType"), str) else request.get("NetworkType")
    if not network_type:
        raise ValidationException("NetworkType is required")

    if store.secondary_networks(ipv4_cidr_block):
        raise ResourceInUseException(f"Resource ipv4_cidr_block already exists")

    record = {
        "ClientToken": client_token,
        "DryRun": dry_run,
        "Ipv4CidrBlock": ipv4_cidr_block,
        "NetworkType": network_type,
        "TagSpecifications": tag_specifications,
    }

    store.secondary_networks(ipv4_cidr_block, record)

    return {
        "SecondaryNetwork": record.get("SecondaryNetwork", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
