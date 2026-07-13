---
id: "@specs/aws/iam/set_security_token_service_preferences"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_SetSecurityTokenServicePreferences"
---

# SetSecurityTokenServicePreferences

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/set_security_token_service_preferences
> **spec:implements:** @kind:operation SetSecurityTokenServicePreferences
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_SetSecurityTokenServicePreferences.spec.md

Sets the specified version of the global endpoint token as the token version used for the Amazon Web Services account. By default, Security Token Service (STS) is available as a global service, and all STS requests go to a single endpoint at https://sts.amazonaws.com . Amazon Web Services recommends using Regional STS endpoints to reduce latency, build in redundancy, and increase session token availability. For information about Regional endpoints for STS, see Security Token Service endpoints and quotas in the Amazon Web Services General Reference . If you make an STS call to the global endpoint, the resulting session tokens might be valid in some Regions but not others. It depends on the version that is set in this operation. Version 1 tokens are valid only in Amazon Web Services Regions that are available by default. These tokens do not work in manually enabled Regions, such as Asia Pacific (Hong Kong). Version 2 tokens are valid in all Regions. However, version 2 tokens are longer and might affect systems where you temporarily store tokens. For information, see Activating and deactivating STS in an Amazon Web Services Region in the IAM User Guide . To view the current session token version, see the GlobalEndpointTokenVersion entry in the response of the GetAccountSummary operation.

## Input Shape: SetSecurityTokenServicePreferencesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GlobalEndpointTokenVersion | Any  # complex shape | ✓ | The version of the global endpoint token. Version 1 tokens are valid only in Amazon Web Services Regions that are availa |

## Errors
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def set_security_token_service_preferences(store, request: dict) -> dict:
    """Sets the specified version of the global endpoint token as the token version used for the Amazon Web Services account. By default, Security Token Service (STS) is available as a global service, and al"""
    global_endpoint_token_version = request.get("GlobalEndpointTokenVersion", "").strip() if isinstance(request.get("GlobalEndpointTokenVersion"), str) else request.get("GlobalEndpointTokenVersion")
    if not global_endpoint_token_version:
        raise ValidationException("GlobalEndpointTokenVersion is required")

    resource = store.set_security_token_service_preferencess(global_endpoint_token_version)
    if not resource:
        raise ResourceNotFoundException(f"Resource global_endpoint_token_version not found")

    # Update mutable fields

    store.set_security_token_service_preferencess(global_endpoint_token_version, resource)
    return resource
```
