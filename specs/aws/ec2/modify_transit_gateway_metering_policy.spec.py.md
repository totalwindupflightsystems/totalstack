---
id: "@specs/aws/ec2/modify_transit_gateway_metering_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyTransitGatewayMeteringPolicy"
---

# ModifyTransitGatewayMeteringPolicy

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_transit_gateway_metering_policy
> **spec:implements:** @kind:operation ModifyTransitGatewayMeteringPolicy
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyTransitGatewayMeteringPolicy.spec.md

Modifies a transit gateway metering policy.

## Input Shape: ModifyTransitGatewayMeteringPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddMiddleboxAttachmentIds | list[Any  # complex shape] |  | The IDs of middlebox attachments to add to the metering policy. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| RemoveMiddleboxAttachmentIds | list[Any  # complex shape] |  | The IDs of middlebox attachments to remove from the metering policy. |
| TransitGatewayMeteringPolicyId | Any  # complex shape | ✓ | The ID of the transit gateway metering policy to modify. |

## Output Shape: ModifyTransitGatewayMeteringPolicyResult

- **TransitGatewayMeteringPolicy** (Any  # complex shape): Information about the modified transit gateway metering policy.

## Implementation

```speclang
def modify_transit_gateway_metering_policy(store, request: dict) -> dict:
    """Modifies a transit gateway metering policy."""
    transit_gateway_metering_policy_id = request.get("TransitGatewayMeteringPolicyId", "").strip() if isinstance(request.get("TransitGatewayMeteringPolicyId"), str) else request.get("TransitGatewayMeteringPolicyId")
    if not transit_gateway_metering_policy_id:
        raise ValidationException("TransitGatewayMeteringPolicyId is required")

    resource = store.transit_gateway_metering_policys(transit_gateway_metering_policy_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource transit_gateway_metering_policy_id not found")

    # Update mutable fields
    if "AddMiddleboxAttachmentIds" in request:
        resource["AddMiddleboxAttachmentIds"] = add_middlebox_attachment_ids
    if "RemoveMiddleboxAttachmentIds" in request:
        resource["RemoveMiddleboxAttachmentIds"] = remove_middlebox_attachment_ids
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.transit_gateway_metering_policys(transit_gateway_metering_policy_id, resource)
    return resource
```
