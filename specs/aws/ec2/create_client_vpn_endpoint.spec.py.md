---
id: "@specs/aws/ec2/create_client_vpn_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateClientVpnEndpoint"
---

# CreateClientVpnEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_client_vpn_endpoint
> **spec:implements:** @kind:operation CreateClientVpnEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateClientVpnEndpoint.spec.md

Creates a Client VPN endpoint. A Client VPN endpoint is the resource you create and configure to enable and manage client VPN sessions. It is the destination endpoint at which all client VPN sessions are terminated.

## Input Shape: CreateClientVpnEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AuthenticationOptions | list[Any  # complex shape] | ✓ | Information about the authentication method to be used to authenticate clients. |
| ClientCidrBlock | str |  | The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap wit |
| ClientConnectOptions | Any  # complex shape |  | The options for managing connection authorization for new client connections. |
| ClientLoginBannerOptions | Any  # complex shape |  | Options for enabling a customizable text banner that will be displayed on Amazon Web Services provided clients when a VP |
| ClientRouteEnforcementOptions | Any  # complex shape |  | Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devic |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| ConnectionLogOptions | Any  # complex shape | ✓ | Information about the client connection logging options. If you enable client connection logging, data about client conn |
| Description | str |  | A brief description of the Client VPN endpoint. |
| DisconnectOnSessionTimeout | bool |  | Indicates whether the client VPN session is disconnected after the maximum timeout specified in SessionTimeoutHours is r |
| DnsServers | list[str] |  | Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. I |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EndpointIpAddressType | Any  # complex shape |  | The IP address type for the Client VPN endpoint. Valid values are ipv4 (default) for IPv4 addressing only, ipv6 for IPv6 |
| SecurityGroupIds | Any  # complex shape |  | The IDs of one or more security groups to apply to the target network. You must also specify the ID of the VPC that cont |
| SelfServicePortal | Any  # complex shape |  | Specify whether to enable the self-service portal for the Client VPN endpoint. Default Value: enabled |
| ServerCertificateArn | str | ✓ | The ARN of the server certificate. For more information, see the Certificate Manager User Guide . |
| SessionTimeoutHours | int |  | The maximum VPN session duration time in hours. Valid values: 8 | 10 | 12 | 24 Default value: 24 |
| SplitTunnel | bool |  | Indicates whether split-tunnel is enabled on the Client VPN endpoint. By default, split-tunnel on a VPN endpoint is disa |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the Client VPN endpoint during creation. |
| TrafficIpAddressType | Any  # complex shape |  | The IP address type for traffic within the Client VPN tunnel. Valid values are ipv4 (default) for IPv4 traffic only, ipv |
| TransportProtocol | Any  # complex shape |  | The transport protocol to be used by the VPN session. Default value: udp |
| VpcId | Any  # complex shape |  | The ID of the VPC to associate with the Client VPN endpoint. If no security group IDs are specified in the request, the  |
| VpnPort | int |  | The port number to assign to the Client VPN endpoint for TCP and UDP traffic. Valid Values: 443 | 1194 Default Value: 44 |

## Output Shape: CreateClientVpnEndpointResult

- **ClientVpnEndpointId** (str): The ID of the Client VPN endpoint.
- **DnsName** (str): The DNS name to be used by clients when establishing their VPN session.
- **Status** (Any  # complex shape): The current state of the Client VPN endpoint.

## Implementation

```speclang
def create_client_vpn_endpoint(store, request: dict) -> dict:
    """Creates a Client VPN endpoint. A Client VPN endpoint is the resource you create and configure to enable and manage client VPN sessions. It is the destination endpoint at which all client VPN sessions """
    authentication_options = request.get("AuthenticationOptions", "").strip() if isinstance(request.get("AuthenticationOptions"), str) else request.get("AuthenticationOptions")
    if not authentication_options:
        raise ValidationException("AuthenticationOptions is required")
    connection_log_options = request.get("ConnectionLogOptions", "").strip() if isinstance(request.get("ConnectionLogOptions"), str) else request.get("ConnectionLogOptions")
    if not connection_log_options:
        raise ValidationException("ConnectionLogOptions is required")
    server_certificate_arn = request.get("ServerCertificateArn", "").strip() if isinstance(request.get("ServerCertificateArn"), str) else request.get("ServerCertificateArn")
    if not server_certificate_arn:
        raise ValidationException("ServerCertificateArn is required")

    if store.client_vpn_endpoints(server_certificate_arn):
        raise ResourceInUseException(f"Resource server_certificate_arn already exists")

    record = {
        "ClientCidrBlock": client_cidr_block,
        "ServerCertificateArn": server_certificate_arn,
        "AuthenticationOptions": authentication_options,
        "ConnectionLogOptions": connection_log_options,
        "DnsServers": dns_servers,
        "TransportProtocol": transport_protocol,
        "VpnPort": vpn_port,
        "Description": description,
        "SplitTunnel": split_tunnel,
        "DryRun": dry_run,
        "ClientToken": client_token,
        "TagSpecifications": tag_specifications,
        "SecurityGroupIds": security_group_ids,
        "VpcId": vpc_id,
        "SelfServicePortal": self_service_portal,
        "ClientConnectOptions": client_connect_options,
        "SessionTimeoutHours": session_timeout_hours,
        "ClientLoginBannerOptions": client_login_banner_options,
        "ClientRouteEnforcementOptions": client_route_enforcement_options,
        "DisconnectOnSessionTimeout": disconnect_on_session_timeout,
        "EndpointIpAddressType": endpoint_ip_address_type,
        "TrafficIpAddressType": traffic_ip_address_type,
    }

    store.client_vpn_endpoints(server_certificate_arn, record)

    return {
        "ClientVpnEndpointId": record.get("ClientVpnEndpointId", {}),
        "Status": record.get("Status", {}),
        "DnsName": record.get("DnsName", {}),
    }
```
