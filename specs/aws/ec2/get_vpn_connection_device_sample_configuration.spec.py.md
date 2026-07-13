---
id: "@specs/aws/ec2/get_vpn_connection_device_sample_configuration"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetVpnConnectionDeviceSampleConfiguration"
---

# GetVpnConnectionDeviceSampleConfiguration

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_vpn_connection_device_sample_configuration
> **spec:implements:** @kind:operation GetVpnConnectionDeviceSampleConfiguration
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetVpnConnectionDeviceSampleConfiguration.spec.md

Download an Amazon Web Services-provided sample configuration file to be used with the customer gateway device specified for your Site-to-Site VPN connection.

## Input Shape: GetVpnConnectionDeviceSampleConfigurationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InternetKeyExchangeVersion | str |  | The IKE version to be used in the sample configuration file for your customer gateway device. You can specify one of the |
| SampleType | str |  | The type of sample configuration to generate. Valid values are "compatibility" (includes IKEv1) or "recommended" (throws |
| VpnConnectionDeviceTypeId | Any  # complex shape | ✓ | Device identifier provided by the GetVpnConnectionDeviceTypes API. |
| VpnConnectionId | Any  # complex shape | ✓ | The VpnConnectionId specifies the Site-to-Site VPN connection used for the sample configuration. |

## Output Shape: GetVpnConnectionDeviceSampleConfigurationResult

- **VpnConnectionDeviceSampleConfiguration** (Any  # complex shape): Sample configuration file for the specified customer gateway device.

## Implementation

```speclang
def get_vpn_connection_device_sample_configuration(store, request: dict) -> dict:
    """Download an Amazon Web Services-provided sample configuration file to be used with the customer gateway device specified for your Site-to-Site VPN connection."""
    vpn_connection_device_type_id = request.get("VpnConnectionDeviceTypeId", "").strip() if isinstance(request.get("VpnConnectionDeviceTypeId"), str) else request.get("VpnConnectionDeviceTypeId")
    if not vpn_connection_device_type_id:
        raise ValidationException("VpnConnectionDeviceTypeId is required")
    vpn_connection_id = request.get("VpnConnectionId", "").strip() if isinstance(request.get("VpnConnectionId"), str) else request.get("VpnConnectionId")
    if not vpn_connection_id:
        raise ValidationException("VpnConnectionId is required")

    resource = store.vpn_connection_device_sample_configurations(vpn_connection_device_type_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpn_connection_device_type_id not found")
    return {"VpnConnectionDeviceTypeId": vpn_connection_device_type_id, **resource}
```
