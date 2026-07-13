---
id: "@specs/aws/ec2/modify_client_vpn_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyClientVpnEndpoint"
---

# ModifyClientVpnEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_client_vpn_endpoint
> **spec:implements:** @kind:operation ModifyClientVpnEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyClientVpnEndpoint.spec.md

Modifies the specified Client VPN endpoint. Modifying the DNS server resets existing client connections.

## Input Shape: ModifyClientVpnEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientConnectOptions | Any  # complex shape |  | The options for managing connection authorization for new client connections. |
| ClientLoginBannerOptions | Any  # complex shape |  | Options for enabling a customizable text banner that will be displayed on Amazon Web Services provided clients when a VP |
| ClientRouteEnforcementOptions | Any  # complex shape |  | Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devic |
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint to modify. |
| ConnectionLogOptions | Any  # complex shape |  | Information about the client connection logging options. If you enable client connection logging, data about client conn |
| Description | str |  | A brief description of the Client VPN endpoint. |
| DisconnectOnSessionTimeout | bool |  | Indicates whether the client VPN session is disconnected after the maximum timeout specified in sessionTimeoutHours is r |
| DnsServers | Any  # complex shape |  | Information about the DNS servers to be used by Client VPN connections. A Client VPN endpoint can have up to two DNS ser |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SecurityGroupIds | Any  # complex shape |  | The IDs of one or more security groups to apply to the target network. |
| SelfServicePortal | Any  # complex shape |  | Specify whether to enable the self-service portal for the Client VPN endpoint. |
| ServerCertificateArn | str |  | The ARN of the server certificate to be used. The server certificate must be provisioned in Certificate Manager (ACM). |
| SessionTimeoutHours | int |  | The maximum VPN session duration time in hours. Valid values: 8 | 10 | 12 | 24 Default value: 24 |
| SplitTunnel | bool |  | Indicates whether the VPN is split-tunnel. For information about split-tunnel VPN endpoints, see Split-tunnel Client VPN |
| VpcId | Any  # complex shape |  | The ID of the VPC to associate with the Client VPN endpoint. |
| VpnPort | int |  | The port number to assign to the Client VPN endpoint for TCP and UDP traffic. Valid Values: 443 | 1194 Default Value: 44 |

## Output Shape: ModifyClientVpnEndpointResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def modify_client_vpn_endpoint(store, request: dict) -> dict:
    """Modifies the specified Client VPN endpoint. Modifying the DNS server resets existing client connections."""
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")
    if not client_vpn_endpoint_id:
        raise ValidationException("ClientVpnEndpointId is required")

    resource = store.client_vpn_endpoints(client_vpn_endpoint_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource client_vpn_endpoint_id not found")

    # Update mutable fields
    if "ServerCertificateArn" in request:
        resource["ServerCertificateArn"] = server_certificate_arn
    if "ConnectionLogOptions" in request:
        resource["ConnectionLogOptions"] = connection_log_options
    if "DnsServers" in request:
        resource["DnsServers"] = dns_servers
    if "VpnPort" in request:
        resource["VpnPort"] = vpn_port
    if "Description" in request:
        resource["Description"] = description
    if "SplitTunnel" in request:
        resource["SplitTunnel"] = split_tunnel
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "SecurityGroupIds" in request:
        resource["SecurityGroupIds"] = security_group_ids
    if "VpcId" in request:
        resource["VpcId"] = vpc_id
    if "SelfServicePortal" in request:
        resource["SelfServicePortal"] = self_service_portal
    if "ClientConnectOptions" in request:
        resource["ClientConnectOptions"] = client_connect_options
    if "SessionTimeoutHours" in request:
        resource["SessionTimeoutHours"] = session_timeout_hours
    if "ClientLoginBannerOptions" in request:
        resource["ClientLoginBannerOptions"] = client_login_banner_options
    if "ClientRouteEnforcementOptions" in request:
        resource["ClientRouteEnforcementOptions"] = client_route_enforcement_options
    if "DisconnectOnSessionTimeout" in request:
        resource["DisconnectOnSessionTimeout"] = disconnect_on_session_timeout

    store.client_vpn_endpoints(client_vpn_endpoint_id, resource)
    return resource
```
