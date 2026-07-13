---
id: "@specs/aws/ec2/associate_trunk_interface"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateTrunkInterface"
---

# AssociateTrunkInterface

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_trunk_interface
> **spec:implements:** @kind:operation AssociateTrunkInterface
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateTrunkInterface.spec.md

Associates a branch network interface with a trunk network interface. Before you create the association, use CreateNetworkInterface command and set the interface type to trunk . You must also create a network interface for each branch network interface that you want to associate with the trunk network interface.

## Input Shape: AssociateTrunkInterfaceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| BranchInterfaceId | Any  # complex shape | ✓ | The ID of the branch network interface. |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GreKey | int |  | The application key. This applies to the GRE protocol. |
| TrunkInterfaceId | Any  # complex shape | ✓ | The ID of the trunk network interface. |
| VlanId | int |  | The ID of the VLAN. This applies to the VLAN protocol. |

## Output Shape: AssociateTrunkInterfaceResult

- **ClientToken** (str): Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E
- **InterfaceAssociation** (Any  # complex shape): Information about the association between the trunk network interface and branch network interface.

## Implementation

```speclang
def associate_trunk_interface(store, request: dict) -> dict:
    """Associates a branch network interface with a trunk network interface. Before you create the association, use CreateNetworkInterface command and set the interface type to trunk . You must also create a"""
    branch_interface_id = request.get("BranchInterfaceId", "").strip() if isinstance(request.get("BranchInterfaceId"), str) else request.get("BranchInterfaceId")
    if not branch_interface_id:
        raise ValidationException("BranchInterfaceId is required")
    trunk_interface_id = request.get("TrunkInterfaceId", "").strip() if isinstance(request.get("TrunkInterfaceId"), str) else request.get("TrunkInterfaceId")
    if not trunk_interface_id:
        raise ValidationException("TrunkInterfaceId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateTrunkInterface", request)
```
