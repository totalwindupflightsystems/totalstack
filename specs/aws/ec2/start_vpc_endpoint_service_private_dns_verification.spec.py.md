---
id: "@specs/aws/ec2/start_vpc_endpoint_service_private_dns_verification"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_StartVpcEndpointServicePrivateDnsVerification"
---

# StartVpcEndpointServicePrivateDnsVerification

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/start_vpc_endpoint_service_private_dns_verification
> **spec:implements:** @kind:operation StartVpcEndpointServicePrivateDnsVerification
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_StartVpcEndpointServicePrivateDnsVerification.spec.md

Initiates the verification process to prove that the service provider owns the private DNS name domain for the endpoint service. The service provider must successfully perform the verification before the consumer can use the name to access the service. Before the service provider runs this command, they must add a record to the DNS server.

## Input Shape: StartVpcEndpointServicePrivateDnsVerificationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ServiceId | Any  # complex shape | ✓ | The ID of the endpoint service. |

## Output Shape: StartVpcEndpointServicePrivateDnsVerificationResult

- **ReturnValue** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def start_vpc_endpoint_service_private_dns_verification(store, request: dict) -> dict:
    """Initiates the verification process to prove that the service provider owns the private DNS name domain for the endpoint service. The service provider must successfully perform the verification before """
    service_id = request.get("ServiceId", "").strip() if isinstance(request.get("ServiceId"), str) else request.get("ServiceId")
    if not service_id:
        raise ValidationException("ServiceId is required")

    if store.vpc_endpoint_service_private_dns_verifications(service_id):
        raise ResourceInUseException(f"Resource service_id already exists")

    record = {
        "DryRun": dry_run,
        "ServiceId": service_id,
    }

    store.vpc_endpoint_service_private_dns_verifications(service_id, record)

    return {
        "ReturnValue": record.get("ReturnValue", {}),
    }
```
