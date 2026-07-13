---
id: "@specs/aws/ec2/modify_vpc_endpoint_service_payer_responsibility"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpcEndpointServicePayerResponsibility"
---

# ModifyVpcEndpointServicePayerResponsibility

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpc_endpoint_service_payer_responsibility
> **spec:implements:** @kind:operation ModifyVpcEndpointServicePayerResponsibility
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpcEndpointServicePayerResponsibility.spec.md

Modifies the payer responsibility for your VPC endpoint service.

## Input Shape: ModifyVpcEndpointServicePayerResponsibilityRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PayerResponsibility | Any  # complex shape | ✓ | The entity that is responsible for the endpoint costs. The default is the endpoint owner. If you set the payer responsib |
| ServiceId | Any  # complex shape | ✓ | The ID of the service. |

## Output Shape: ModifyVpcEndpointServicePayerResponsibilityResult

- **ReturnValue** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def modify_vpc_endpoint_service_payer_responsibility(store, request: dict) -> dict:
    """Modifies the payer responsibility for your VPC endpoint service."""
    payer_responsibility = request.get("PayerResponsibility", "").strip() if isinstance(request.get("PayerResponsibility"), str) else request.get("PayerResponsibility")
    if not payer_responsibility:
        raise ValidationException("PayerResponsibility is required")
    service_id = request.get("ServiceId", "").strip() if isinstance(request.get("ServiceId"), str) else request.get("ServiceId")
    if not service_id:
        raise ValidationException("ServiceId is required")

    resource = store.vpc_endpoint_service_payer_responsibilitys(service_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource service_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.vpc_endpoint_service_payer_responsibilitys(service_id, resource)
    return resource
```
