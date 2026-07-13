---
id: "@specs/aws/ec2/associate_transit_gateway_policy_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateTransitGatewayPolicyTable"
---

# AssociateTransitGatewayPolicyTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_transit_gateway_policy_table
> **spec:implements:** @kind:operation AssociateTransitGatewayPolicyTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateTransitGatewayPolicyTable.spec.md

Associates the specified transit gateway attachment with a transit gateway policy table.

## Input Shape: AssociateTransitGatewayPolicyTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the transit gateway attachment to associate with the policy table. |
| TransitGatewayPolicyTableId | Any  # complex shape | ✓ | The ID of the transit gateway policy table to associate with the transit gateway attachment. |

## Output Shape: AssociateTransitGatewayPolicyTableResult

- **Association** (Any  # complex shape): Describes the association of a transit gateway and a transit gateway policy table.

## Implementation

```speclang
def associate_transit_gateway_policy_table(store, request: dict) -> dict:
    """Associates the specified transit gateway attachment with a transit gateway policy table."""
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")
    if not transit_gateway_attachment_id:
        raise ValidationException("TransitGatewayAttachmentId is required")
    transit_gateway_policy_table_id = request.get("TransitGatewayPolicyTableId", "").strip() if isinstance(request.get("TransitGatewayPolicyTableId"), str) else request.get("TransitGatewayPolicyTableId")
    if not transit_gateway_policy_table_id:
        raise ValidationException("TransitGatewayPolicyTableId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateTransitGatewayPolicyTable", request)
```
