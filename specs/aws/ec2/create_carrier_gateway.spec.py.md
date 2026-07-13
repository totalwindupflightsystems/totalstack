---
id: "@specs/aws/ec2/create_carrier_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateCarrierGateway"
---

# CreateCarrierGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_carrier_gateway
> **spec:implements:** @kind:operation CreateCarrierGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateCarrierGateway.spec.md

Creates a carrier gateway. For more information about carrier gateways, see Carrier gateways in the Amazon Web Services Wavelength Developer Guide .

## Input Shape: CreateCarrierGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | The tags to associate with the carrier gateway. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC to associate with the carrier gateway. |

## Output Shape: CreateCarrierGatewayResult

- **CarrierGateway** (Any  # complex shape): Information about the carrier gateway.

## Implementation

```speclang
def create_carrier_gateway(store, request: dict) -> dict:
    """Creates a carrier gateway. For more information about carrier gateways, see Carrier gateways in the Amazon Web Services Wavelength Developer Guide ."""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    if store.carrier_gateways(vpc_id):
        raise ResourceInUseException(f"Resource vpc_id already exists")

    record = {
        "VpcId": vpc_id,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
        "ClientToken": client_token,
    }

    store.carrier_gateways(vpc_id, record)

    return {
        "CarrierGateway": record.get("CarrierGateway", {}),
    }
```
