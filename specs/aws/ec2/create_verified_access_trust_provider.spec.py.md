---
id: "@specs/aws/ec2/create_verified_access_trust_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVerifiedAccessTrustProvider"
---

# CreateVerifiedAccessTrustProvider

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_verified_access_trust_provider
> **spec:implements:** @kind:operation CreateVerifiedAccessTrustProvider
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVerifiedAccessTrustProvider.spec.md

A trust provider is a third-party entity that creates, maintains, and manages identity information for users and devices. When an application request is made, the identity information sent by the trust provider is evaluated by Verified Access before allowing or denying the application request.

## Input Shape: CreateVerifiedAccessTrustProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| Description | str |  | A description for the Verified Access trust provider. |
| DeviceOptions | Any  # complex shape |  | The options for a device-based trust provider. This parameter is required when the provider type is device . |
| DeviceTrustProviderType | Any  # complex shape |  | The type of device-based trust provider. This parameter is required when the provider type is device . |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NativeApplicationOidcOptions | Any  # complex shape |  | The OpenID Connect (OIDC) options. |
| OidcOptions | Any  # complex shape |  | The options for a OpenID Connect-compatible user-identity trust provider. This parameter is required when the provider t |
| PolicyReferenceName | str | ✓ | The identifier to be used when working with policy rules. |
| SseSpecification | Any  # complex shape |  | The options for server side encryption. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the Verified Access trust provider. |
| TrustProviderType | Any  # complex shape | ✓ | The type of trust provider. |
| UserTrustProviderType | Any  # complex shape |  | The type of user-based trust provider. This parameter is required when the provider type is user . |

## Output Shape: CreateVerifiedAccessTrustProviderResult

- **VerifiedAccessTrustProvider** (Any  # complex shape): Details about the Verified Access trust provider.

## Implementation

```speclang
def create_verified_access_trust_provider(store, request: dict) -> dict:
    """A trust provider is a third-party entity that creates, maintains, and manages identity information for users and devices. When an application request is made, the identity information sent by the trus"""
    policy_reference_name = request.get("PolicyReferenceName", "").strip() if isinstance(request.get("PolicyReferenceName"), str) else request.get("PolicyReferenceName")
    if not policy_reference_name:
        raise ValidationException("PolicyReferenceName is required")
    trust_provider_type = request.get("TrustProviderType", "").strip() if isinstance(request.get("TrustProviderType"), str) else request.get("TrustProviderType")
    if not trust_provider_type:
        raise ValidationException("TrustProviderType is required")

    if store.verified_access_trust_providers(trust_provider_type):
        raise ResourceInUseException(f"Resource trust_provider_type already exists")

    record = {
        "TrustProviderType": trust_provider_type,
        "UserTrustProviderType": user_trust_provider_type,
        "DeviceTrustProviderType": device_trust_provider_type,
        "OidcOptions": oidc_options,
        "DeviceOptions": device_options,
        "PolicyReferenceName": policy_reference_name,
        "Description": description,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
        "DryRun": dry_run,
        "SseSpecification": sse_specification,
        "NativeApplicationOidcOptions": native_application_oidc_options,
    }

    store.verified_access_trust_providers(trust_provider_type, record)

    return {
        "VerifiedAccessTrustProvider": record.get("VerifiedAccessTrustProvider", {}),
    }
```
