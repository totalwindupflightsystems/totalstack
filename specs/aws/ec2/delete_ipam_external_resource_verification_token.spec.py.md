---
id: "@specs/aws/ec2/delete_ipam_external_resource_verification_token"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteIpamExternalResourceVerificationToken"
---

# DeleteIpamExternalResourceVerificationToken

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_ipam_external_resource_verification_token
> **spec:implements:** @kind:operation DeleteIpamExternalResourceVerificationToken
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteIpamExternalResourceVerificationToken.spec.md

Delete a verification token. A verification token is an Amazon Web Services-generated random value that you can use to prove ownership of an external resource. For example, you can use a verification token to validate that you control a public IP address range when you bring an IP address range to Amazon Web Services (BYOIP).

## Input Shape: DeleteIpamExternalResourceVerificationTokenRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamExternalResourceVerificationTokenId | Any  # complex shape | ✓ | The token ID. |

## Output Shape: DeleteIpamExternalResourceVerificationTokenResult

- **IpamExternalResourceVerificationToken** (Any  # complex shape): The verification token.

## Implementation

```speclang
def delete_ipam_external_resource_verification_token(store, request: dict) -> dict:
    """Delete a verification token. A verification token is an Amazon Web Services-generated random value that you can use to prove ownership of an external resource. For example, you can use a verification """
    ipam_external_resource_verification_token_id = request.get("IpamExternalResourceVerificationTokenId", "").strip() if isinstance(request.get("IpamExternalResourceVerificationTokenId"), str) else request.get("IpamExternalResourceVerificationTokenId")

    if not store.ipam_external_resource_verification_tokens(ipam_external_resource_verification_token_id):
        raise ResourceNotFoundException(f"Resource ipam_external_resource_verification_token_id not found")
    store.delete_ipam_external_resource_verification_tokens(ipam_external_resource_verification_token_id)
    return {}
```
