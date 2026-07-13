---
id: "@specs/aws/ec2/export_verified_access_instance_client_configuration"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ExportVerifiedAccessInstanceClientConfiguration"
---

# ExportVerifiedAccessInstanceClientConfiguration

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/export_verified_access_instance_client_configuration
> **spec:implements:** @kind:operation ExportVerifiedAccessInstanceClientConfiguration
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ExportVerifiedAccessInstanceClientConfiguration.spec.md

Exports the client configuration for a Verified Access instance.

## Input Shape: ExportVerifiedAccessInstanceClientConfigurationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VerifiedAccessInstanceId | Any  # complex shape | ✓ | The ID of the Verified Access instance. |

## Output Shape: ExportVerifiedAccessInstanceClientConfigurationResult

- **DeviceTrustProviders** (list[Any  # complex shape]): The device trust providers.
- **OpenVpnConfigurations** (list[Any  # complex shape]): The Open VPN configuration.
- **Region** (str): The Region.
- **UserTrustProvider** (Any  # complex shape): The user identity trust provider.
- **VerifiedAccessInstanceId** (str): The ID of the Verified Access instance.
- **Version** (str): The version.

## Implementation

```speclang
def export_verified_access_instance_client_configuration(store, request: dict) -> dict:
    """Exports the client configuration for a Verified Access instance."""
    verified_access_instance_id = request.get("VerifiedAccessInstanceId", "").strip() if isinstance(request.get("VerifiedAccessInstanceId"), str) else request.get("VerifiedAccessInstanceId")
    if not verified_access_instance_id:
        raise ValidationException("VerifiedAccessInstanceId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ExportVerifiedAccessInstanceClientConfiguration", request)
```
