---
id: "@specs/aws/ec2/attach_internet_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AttachInternetGateway"
---

# AttachInternetGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/attach_internet_gateway
> **spec:implements:** @kind:operation AttachInternetGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AttachInternetGateway.spec.md

Attaches an internet gateway or a virtual private gateway to a VPC, enabling connectivity between the internet and the VPC. For more information, see Internet gateways in the Amazon VPC User Guide .

## Input Shape: AttachInternetGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InternetGatewayId | Any  # complex shape | ✓ | The ID of the internet gateway. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Implementation

```speclang
def attach_internet_gateway(store, request: dict) -> dict:
    """Attaches an internet gateway or a virtual private gateway to a VPC, enabling connectivity between the internet and the VPC. For more information, see Internet gateways in the Amazon VPC User Guide ."""
    internet_gateway_id = request.get("InternetGatewayId", "").strip() if isinstance(request.get("InternetGatewayId"), str) else request.get("InternetGatewayId")
    if not internet_gateway_id:
        raise ValidationException("InternetGatewayId is required")
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachInternetGateway", request)
```
