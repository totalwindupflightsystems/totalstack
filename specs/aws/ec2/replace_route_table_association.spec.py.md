---
id: "@specs/aws/ec2/replace_route_table_association"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ReplaceRouteTableAssociation"
---

# ReplaceRouteTableAssociation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/replace_route_table_association
> **spec:implements:** @kind:operation ReplaceRouteTableAssociation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ReplaceRouteTableAssociation.spec.md

Changes the route table associated with a given subnet, internet gateway, or virtual private gateway in a VPC. After the operation completes, the subnet or gateway uses the routes in the new route table. For more information about route tables, see Route tables in the Amazon VPC User Guide . You can also use this operation to change which table is the main route table in the VPC. Specify the main route table's association ID and the route table ID of the new main route table.

## Input Shape: ReplaceRouteTableAssociationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationId | Any  # complex shape | ✓ | The association ID. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| RouteTableId | Any  # complex shape | ✓ | The ID of the new route table to associate with the subnet. |

## Output Shape: ReplaceRouteTableAssociationResult

- **AssociationState** (Any  # complex shape): The state of the association.
- **NewAssociationId** (str): The ID of the new association.

## Implementation

```speclang
def replace_route_table_association(store, request: dict) -> dict:
    """Changes the route table associated with a given subnet, internet gateway, or virtual private gateway in a VPC. After the operation completes, the subnet or gateway uses the routes in the new route tab"""
    association_id = request.get("AssociationId", "").strip() if isinstance(request.get("AssociationId"), str) else request.get("AssociationId")
    if not association_id:
        raise ValidationException("AssociationId is required")
    route_table_id = request.get("RouteTableId", "").strip() if isinstance(request.get("RouteTableId"), str) else request.get("RouteTableId")
    if not route_table_id:
        raise ValidationException("RouteTableId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ReplaceRouteTableAssociation", request)
```
