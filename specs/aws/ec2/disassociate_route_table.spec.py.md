---
id: "@specs/aws/ec2/disassociate_route_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateRouteTable"
---

# DisassociateRouteTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_route_table
> **spec:implements:** @kind:operation DisassociateRouteTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateRouteTable.spec.md

Disassociates a subnet or gateway from a route table. After you perform this action, the subnet no longer uses the routes in the route table. Instead, it uses the routes in the VPC's main route table. For more information about route tables, see Route tables in the Amazon VPC User Guide .

## Input Shape: DisassociateRouteTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationId | Any  # complex shape | ✓ | The association ID representing the current association between the route table and subnet or gateway. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Implementation

```speclang
def disassociate_route_table(store, request: dict) -> dict:
    """Disassociates a subnet or gateway from a route table. After you perform this action, the subnet no longer uses the routes in the route table. Instead, it uses the routes in the VPC's main route table."""
    association_id = request.get("AssociationId", "").strip() if isinstance(request.get("AssociationId"), str) else request.get("AssociationId")
    if not association_id:
        raise ValidationException("AssociationId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DisassociateRouteTable", request)
```
