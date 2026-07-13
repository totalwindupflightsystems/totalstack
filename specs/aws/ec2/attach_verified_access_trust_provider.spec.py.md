---
id: "@specs/aws/ec2/attach_verified_access_trust_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AttachVerifiedAccessTrustProvider"
---

# AttachVerifiedAccessTrustProvider

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/attach_verified_access_trust_provider
> **spec:implements:** @kind:operation AttachVerifiedAccessTrustProvider
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AttachVerifiedAccessTrustProvider.spec.md

Attaches the specified Amazon Web Services Verified Access trust provider to the specified Amazon Web Services Verified Access instance.

## Input Shape: AttachVerifiedAccessTrustProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VerifiedAccessInstanceId | Any  # complex shape | ✓ | The ID of the Verified Access instance. |
| VerifiedAccessTrustProviderId | Any  # complex shape | ✓ | The ID of the Verified Access trust provider. |

## Output Shape: AttachVerifiedAccessTrustProviderResult

- **VerifiedAccessInstance** (Any  # complex shape): Details about the Verified Access instance.
- **VerifiedAccessTrustProvider** (Any  # complex shape): Details about the Verified Access trust provider.

## Implementation

```speclang
def attach_verified_access_trust_provider(store, request: dict) -> dict:
    """Attaches the specified Amazon Web Services Verified Access trust provider to the specified Amazon Web Services Verified Access instance."""
    verified_access_instance_id = request.get("VerifiedAccessInstanceId", "").strip() if isinstance(request.get("VerifiedAccessInstanceId"), str) else request.get("VerifiedAccessInstanceId")
    if not verified_access_instance_id:
        raise ValidationException("VerifiedAccessInstanceId is required")
    verified_access_trust_provider_id = request.get("VerifiedAccessTrustProviderId", "").strip() if isinstance(request.get("VerifiedAccessTrustProviderId"), str) else request.get("VerifiedAccessTrustProviderId")
    if not verified_access_trust_provider_id:
        raise ValidationException("VerifiedAccessTrustProviderId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachVerifiedAccessTrustProvider", request)
```
