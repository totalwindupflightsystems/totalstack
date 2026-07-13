---
id: "@specs/aws/ec2/create_ipam_external_resource_verification_token"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateIpamExternalResourceVerificationToken"
---

# CreateIpamExternalResourceVerificationToken

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_ipam_external_resource_verification_token
> **spec:implements:** @kind:operation CreateIpamExternalResourceVerificationToken
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateIpamExternalResourceVerificationToken.spec.md

Create a verification token. A verification token is an Amazon Web Services-generated random value that you can use to prove ownership of an external resource. For example, you can use a verification token to validate that you control a public IP address range when you bring an IP address range to Amazon Web Services (BYOIP).

## Input Shape: CreateIpamExternalResourceVerificationTokenRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamId | Any  # complex shape | ✓ | The ID of the IPAM that will create the token. |
| TagSpecifications | list[Any  # complex shape] |  | Token tags. |

## Output Shape: CreateIpamExternalResourceVerificationTokenResult

- **IpamExternalResourceVerificationToken** (Any  # complex shape): The verification token.

## Implementation

```speclang
def create_ipam_external_resource_verification_token(store, request: dict) -> dict:
    """Create a verification token. A verification token is an Amazon Web Services-generated random value that you can use to prove ownership of an external resource. For example, you can use a verification """
    ipam_id = request.get("IpamId", "").strip() if isinstance(request.get("IpamId"), str) else request.get("IpamId")
    if not ipam_id:
        raise ValidationException("IpamId is required")

    if store.ipam_external_resource_verification_tokens(ipam_id):
        raise ResourceInUseException(f"Resource ipam_id already exists")

    record = {
        "DryRun": dry_run,
        "IpamId": ipam_id,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
    }

    store.ipam_external_resource_verification_tokens(ipam_id, record)

    return {
        "IpamExternalResourceVerificationToken": record.get("IpamExternalResourceVerificationToken", {}),
    }
```
