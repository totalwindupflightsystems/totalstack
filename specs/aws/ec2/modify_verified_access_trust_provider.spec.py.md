---
id: "@specs/aws/ec2/modify_verified_access_trust_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVerifiedAccessTrustProvider"
---

# ModifyVerifiedAccessTrustProvider

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_verified_access_trust_provider
> **spec:implements:** @kind:operation ModifyVerifiedAccessTrustProvider
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVerifiedAccessTrustProvider.spec.md

Modifies the configuration of the specified Amazon Web Services Verified Access trust provider.

## Input Shape: ModifyVerifiedAccessTrustProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| Description | str |  | A description for the Verified Access trust provider. |
| DeviceOptions | Any  # complex shape |  | The options for a device-based trust provider. This parameter is required when the provider type is device . |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NativeApplicationOidcOptions | Any  # complex shape |  | The OpenID Connect (OIDC) options. |
| OidcOptions | Any  # complex shape |  | The options for an OpenID Connect-compatible user-identity trust provider. |
| SseSpecification | Any  # complex shape |  | The options for server side encryption. |
| VerifiedAccessTrustProviderId | Any  # complex shape | ✓ | The ID of the Verified Access trust provider. |

## Output Shape: ModifyVerifiedAccessTrustProviderResult

- **VerifiedAccessTrustProvider** (Any  # complex shape): Details about the Verified Access trust provider.

## Implementation

```speclang
def modify_verified_access_trust_provider(store, request: dict) -> dict:
    """Modifies the configuration of the specified Amazon Web Services Verified Access trust provider."""
    verified_access_trust_provider_id = request.get("VerifiedAccessTrustProviderId", "").strip() if isinstance(request.get("VerifiedAccessTrustProviderId"), str) else request.get("VerifiedAccessTrustProviderId")
    if not verified_access_trust_provider_id:
        raise ValidationException("VerifiedAccessTrustProviderId is required")

    resource = store.verified_access_trust_providers(verified_access_trust_provider_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource verified_access_trust_provider_id not found")

    # Update mutable fields
    if "OidcOptions" in request:
        resource["OidcOptions"] = oidc_options
    if "DeviceOptions" in request:
        resource["DeviceOptions"] = device_options
    if "Description" in request:
        resource["Description"] = description
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "ClientToken" in request:
        resource["ClientToken"] = client_token
    if "SseSpecification" in request:
        resource["SseSpecification"] = sse_specification
    if "NativeApplicationOidcOptions" in request:
        resource["NativeApplicationOidcOptions"] = native_application_oidc_options

    store.verified_access_trust_providers(verified_access_trust_provider_id, resource)
    return resource
```
