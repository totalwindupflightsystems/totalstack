---
id: "@specs/aws/ec2/create_transit_gateway_metering_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGatewayMeteringPolicy"
---

# CreateTransitGatewayMeteringPolicy

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway_metering_policy
> **spec:implements:** @kind:operation CreateTransitGatewayMeteringPolicy
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGatewayMeteringPolicy.spec.md

Creates a metering policy for a transit gateway to track and measure network traffic.

## Input Shape: CreateTransitGatewayMeteringPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MiddleboxAttachmentIds | list[Any  # complex shape] |  | The IDs of the middlebox attachments to include in the metering policy. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the metering policy. |
| TransitGatewayId | Any  # complex shape | ✓ | The ID of the transit gateway for which to create the metering policy. |

## Output Shape: CreateTransitGatewayMeteringPolicyResult

- **TransitGatewayMeteringPolicy** (Any  # complex shape): Information about the created transit gateway metering policy.

## Implementation

```speclang
def create_transit_gateway_metering_policy(store, request: dict) -> dict:
    """Creates a metering policy for a transit gateway to track and measure network traffic."""
    transit_gateway_id = request.get("TransitGatewayId", "").strip() if isinstance(request.get("TransitGatewayId"), str) else request.get("TransitGatewayId")
    if not transit_gateway_id:
        raise ValidationException("TransitGatewayId is required")

    if store.transit_gateway_metering_policys(transit_gateway_id):
        raise ResourceInUseException(f"Resource transit_gateway_id already exists")

    record = {
        "TransitGatewayId": transit_gateway_id,
        "MiddleboxAttachmentIds": middlebox_attachment_ids,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.transit_gateway_metering_policys(transit_gateway_id, record)

    return {
        "TransitGatewayMeteringPolicy": record.get("TransitGatewayMeteringPolicy", {}),
    }
```
