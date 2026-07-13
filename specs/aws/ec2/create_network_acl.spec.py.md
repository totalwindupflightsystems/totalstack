---
id: "@specs/aws/ec2/create_network_acl"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateNetworkAcl"
---

# CreateNetworkAcl

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_network_acl
> **spec:implements:** @kind:operation CreateNetworkAcl
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateNetworkAcl.spec.md

Creates a network ACL in a VPC. Network ACLs provide an optional layer of security (in addition to security groups) for the instances in your VPC. For more information, see Network ACLs in the Amazon VPC User Guide .

## Input Shape: CreateNetworkAclRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the network ACL. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Output Shape: CreateNetworkAclResult

- **ClientToken** (str): Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided
- **NetworkAcl** (Any  # complex shape): Information about the network ACL.

## Implementation

```speclang
def create_network_acl(store, request: dict) -> dict:
    """Creates a network ACL in a VPC. Network ACLs provide an optional layer of security (in addition to security groups) for the instances in your VPC. For more information, see Network ACLs in the Amazon """
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    if store.network_acls(vpc_id):
        raise ResourceInUseException(f"Resource vpc_id already exists")

    record = {
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
        "DryRun": dry_run,
        "VpcId": vpc_id,
    }

    store.network_acls(vpc_id, record)

    return {
        "NetworkAcl": record.get("NetworkAcl", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
