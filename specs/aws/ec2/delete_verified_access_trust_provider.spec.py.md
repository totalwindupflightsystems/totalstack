---
id: "@specs/aws/ec2/delete_verified_access_trust_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVerifiedAccessTrustProvider"
---

# DeleteVerifiedAccessTrustProvider

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_verified_access_trust_provider
> **spec:implements:** @kind:operation DeleteVerifiedAccessTrustProvider
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVerifiedAccessTrustProvider.spec.md

Delete an Amazon Web Services Verified Access trust provider.

## Input Shape: DeleteVerifiedAccessTrustProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VerifiedAccessTrustProviderId | Any  # complex shape | ✓ | The ID of the Verified Access trust provider. |

## Output Shape: DeleteVerifiedAccessTrustProviderResult

- **VerifiedAccessTrustProvider** (Any  # complex shape): Details about the Verified Access trust provider.

## Implementation

```speclang
def delete_verified_access_trust_provider(store, request: dict) -> dict:
    """Delete an Amazon Web Services Verified Access trust provider."""
    verified_access_trust_provider_id = request.get("VerifiedAccessTrustProviderId", "").strip() if isinstance(request.get("VerifiedAccessTrustProviderId"), str) else request.get("VerifiedAccessTrustProviderId")

    if not store.verified_access_trust_providers(verified_access_trust_provider_id):
        raise ResourceNotFoundException(f"Resource verified_access_trust_provider_id not found")
    store.delete_verified_access_trust_providers(verified_access_trust_provider_id)
    return {}
```
