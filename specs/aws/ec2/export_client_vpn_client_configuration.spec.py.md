---
id: "@specs/aws/ec2/export_client_vpn_client_configuration"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ExportClientVpnClientConfiguration"
---

# ExportClientVpnClientConfiguration

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/export_client_vpn_client_configuration
> **spec:implements:** @kind:operation ExportClientVpnClientConfiguration
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ExportClientVpnClientConfiguration.spec.md

Downloads the contents of the Client VPN endpoint configuration file for the specified Client VPN endpoint. The Client VPN endpoint configuration file includes the Client VPN endpoint and certificate information clients need to establish a connection with the Client VPN endpoint.

## Input Shape: ExportClientVpnClientConfigurationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: ExportClientVpnClientConfigurationResult

- **ClientConfiguration** (str): The contents of the Client VPN endpoint configuration file.

## Implementation

```speclang
def export_client_vpn_client_configuration(store, request: dict) -> dict:
    """Downloads the contents of the Client VPN endpoint configuration file for the specified Client VPN endpoint. The Client VPN endpoint configuration file includes the Client VPN endpoint and certificate """
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")
    if not client_vpn_endpoint_id:
        raise ValidationException("ClientVpnEndpointId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ExportClientVpnClientConfiguration", request)
```
