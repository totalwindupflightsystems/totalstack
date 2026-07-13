---
id: "@specs/aws/ec2/get_vpn_connection_device_types"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetVpnConnectionDeviceTypes"
---

# GetVpnConnectionDeviceTypes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_vpn_connection_device_types
> **spec:implements:** @kind:operation GetVpnConnectionDeviceTypes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetVpnConnectionDeviceTypes.spec.md

Obtain a list of customer gateway devices for which sample configuration files can be provided. The request has no additional parameters. You can also see the list of device types with sample configuration files available under Your customer gateway device in the Amazon Web Services Site-to-Site VPN User Guide .

## Input Shape: GetVpnConnectionDeviceTypesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of results returned by GetVpnConnectionDeviceTypes in paginated output. When this parameter is used,  |
| NextToken | Any  # complex shape |  | The NextToken value returned from a previous paginated GetVpnConnectionDeviceTypes request where MaxResults was used and |

## Output Shape: GetVpnConnectionDeviceTypesResult

- **NextToken** (Any  # complex shape): The NextToken value to include in a future GetVpnConnectionDeviceTypes request. When the results of a GetVpnConnectionDe
- **VpnConnectionDeviceTypes** (list[Any  # complex shape]): List of customer gateway devices that have a sample configuration file available for use.

## Implementation

```speclang
def get_vpn_connection_device_types(store, request: dict) -> dict:
    """Obtain a list of customer gateway devices for which sample configuration files can be provided. The request has no additional parameters. You can also see the list of device types with sample configur"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
