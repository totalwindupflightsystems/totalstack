---
id: "@specs/aws/ec2/create_transit_gateway_metering_policy_entry"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGatewayMeteringPolicyEntry"
---

# CreateTransitGatewayMeteringPolicyEntry

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway_metering_policy_entry
> **spec:implements:** @kind:operation CreateTransitGatewayMeteringPolicyEntry
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGatewayMeteringPolicyEntry.spec.md

Creates an entry in a transit gateway metering policy to define traffic measurement rules.

## Input Shape: CreateTransitGatewayMeteringPolicyEntryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DestinationCidrBlock | str |  | The destination CIDR block for traffic matching. |
| DestinationPortRange | str |  | The destination port range for traffic matching. |
| DestinationTransitGatewayAttachmentId | Any  # complex shape |  | The ID of the destination transit gateway attachment for traffic matching. |
| DestinationTransitGatewayAttachmentType | Any  # complex shape |  | The type of the destination transit gateway attachment for traffic matching. Note that the tgw-peering resource type has |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MeteredAccount | Any  # complex shape | ✓ | The Amazon Web Services account ID to which the metered traffic should be attributed. |
| PolicyRuleNumber | int | ✓ | The rule number for the metering policy entry. Rules are processed in order from lowest to highest number. |
| Protocol | str |  | The protocol for traffic matching (1, 6, 17, etc.). |
| SourceCidrBlock | str |  | The source CIDR block for traffic matching. |
| SourcePortRange | str |  | The source port range for traffic matching. |
| SourceTransitGatewayAttachmentId | Any  # complex shape |  | The ID of the source transit gateway attachment for traffic matching. |
| SourceTransitGatewayAttachmentType | Any  # complex shape |  | The type of the source transit gateway attachment for traffic matching. Note that the tgw-peering resource type has been |
| TransitGatewayMeteringPolicyId | Any  # complex shape | ✓ | The ID of the transit gateway metering policy to add the entry to. |

## Output Shape: CreateTransitGatewayMeteringPolicyEntryResult

- **TransitGatewayMeteringPolicyEntry** (Any  # complex shape): Information about the created transit gateway metering policy entry.

## Implementation

```speclang
def create_transit_gateway_metering_policy_entry(store, request: dict) -> dict:
    """Creates an entry in a transit gateway metering policy to define traffic measurement rules."""
    metered_account = request.get("MeteredAccount", "").strip() if isinstance(request.get("MeteredAccount"), str) else request.get("MeteredAccount")
    if not metered_account:
        raise ValidationException("MeteredAccount is required")
    policy_rule_number = request.get("PolicyRuleNumber", "").strip() if isinstance(request.get("PolicyRuleNumber"), str) else request.get("PolicyRuleNumber")
    if not policy_rule_number:
        raise ValidationException("PolicyRuleNumber is required")
    transit_gateway_metering_policy_id = request.get("TransitGatewayMeteringPolicyId", "").strip() if isinstance(request.get("TransitGatewayMeteringPolicyId"), str) else request.get("TransitGatewayMeteringPolicyId")
    if not transit_gateway_metering_policy_id:
        raise ValidationException("TransitGatewayMeteringPolicyId is required")

    if store.transit_gateway_metering_policy_entrys(transit_gateway_metering_policy_id):
        raise ResourceInUseException(f"Resource transit_gateway_metering_policy_id already exists")

    record = {
        "TransitGatewayMeteringPolicyId": transit_gateway_metering_policy_id,
        "PolicyRuleNumber": policy_rule_number,
        "SourceTransitGatewayAttachmentId": source_transit_gateway_attachment_id,
        "SourceTransitGatewayAttachmentType": source_transit_gateway_attachment_type,
        "SourceCidrBlock": source_cidr_block,
        "SourcePortRange": source_port_range,
        "DestinationTransitGatewayAttachmentId": destination_transit_gateway_attachment_id,
        "DestinationTransitGatewayAttachmentType": destination_transit_gateway_attachment_type,
        "DestinationCidrBlock": destination_cidr_block,
        "DestinationPortRange": destination_port_range,
        "Protocol": protocol,
        "MeteredAccount": metered_account,
        "DryRun": dry_run,
    }

    store.transit_gateway_metering_policy_entrys(transit_gateway_metering_policy_id, record)

    return {
        "TransitGatewayMeteringPolicyEntry": record.get("TransitGatewayMeteringPolicyEntry", {}),
    }
```
