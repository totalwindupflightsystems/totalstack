---
id: "@specs/aws/ec2/disassociate_transit_gateway_policy_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateTransitGatewayPolicyTable"
---

# DisassociateTransitGatewayPolicyTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_transit_gateway_policy_table
> **spec:implements:** @kind:operation DisassociateTransitGatewayPolicyTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateTransitGatewayPolicyTable.spec.md

Removes the association between an an attachment and a policy table.

## Input Shape: DisassociateTransitGatewayPolicyTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the transit gateway attachment to disassociate from the policy table. |
| TransitGatewayPolicyTableId | Any  # complex shape | ✓ | The ID of the disassociated policy table. |

## Output Shape: DisassociateTransitGatewayPolicyTableResult

- **Association** (Any  # complex shape): Returns details about the transit gateway policy table disassociation.

## Implementation

```speclang
def disassociate_transit_gateway_policy_table(store, request: dict) -> dict:
    """Removes the association between an an attachment and a policy table."""
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")
    if not transit_gateway_attachment_id:
        raise ValidationException("TransitGatewayAttachmentId is required")
    transit_gateway_policy_table_id = request.get("TransitGatewayPolicyTableId", "").strip() if isinstance(request.get("TransitGatewayPolicyTableId"), str) else request.get("TransitGatewayPolicyTableId")
    if not transit_gateway_policy_table_id:
        raise ValidationException("TransitGatewayPolicyTableId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DisassociateTransitGatewayPolicyTable", request)
```
