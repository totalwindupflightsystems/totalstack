---
id: "@specs/aws/ec2/create_vpc_endpoint_service_configuration"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVpcEndpointServiceConfiguration"
---

# CreateVpcEndpointServiceConfiguration

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_vpc_endpoint_service_configuration
> **spec:implements:** @kind:operation CreateVpcEndpointServiceConfiguration
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVpcEndpointServiceConfiguration.spec.md

Creates a VPC endpoint service to which service consumers (Amazon Web Services accounts, users, and IAM roles) can connect. Before you create an endpoint service, you must create one of the following for your service: A Network Load Balancer . Service consumers connect to your service using an interface endpoint. A Gateway Load Balancer . Service consumers connect to your service using a Gateway Load Balancer endpoint. If you set the private DNS name, you must prove that you own the private DNS domain name. For more information, see the Amazon Web Services PrivateLink Guide .

## Input Shape: CreateVpcEndpointServiceConfigurationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AcceptanceRequired | bool |  | Indicates whether requests from service consumers to create an endpoint to your service must be accepted manually. |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GatewayLoadBalancerArns | list[str] |  | The Amazon Resource Names (ARNs) of the Gateway Load Balancers. |
| NetworkLoadBalancerArns | list[str] |  | The Amazon Resource Names (ARNs) of the Network Load Balancers. |
| PrivateDnsName | str |  | (Interface endpoint configuration) The private DNS name to assign to the VPC endpoint service. |
| SupportedIpAddressTypes | list[str] |  | The supported IP address types. The possible values are ipv4 and ipv6 . |
| SupportedRegions | list[str] |  | The Regions from which service consumers can access the service. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to associate with the service. |

## Output Shape: CreateVpcEndpointServiceConfigurationResult

- **ClientToken** (str): Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
- **ServiceConfiguration** (Any  # complex shape): Information about the service configuration.

## Implementation

```speclang
def create_vpc_endpoint_service_configuration(store, request: dict) -> dict:
    """Creates a VPC endpoint service to which service consumers (Amazon Web Services accounts, users, and IAM roles) can connect. Before you create an endpoint service, you must create one of the following """


    record = {
        "DryRun": dry_run,
        "AcceptanceRequired": acceptance_required,
        "PrivateDnsName": private_dns_name,
        "NetworkLoadBalancerArns": network_load_balancer_arns,
        "GatewayLoadBalancerArns": gateway_load_balancer_arns,
        "SupportedIpAddressTypes": supported_ip_address_types,
        "SupportedRegions": supported_regions,
        "ClientToken": client_token,
        "TagSpecifications": tag_specifications,
    }

    store.vpc_endpoint_service_configurations(record)

    return {
        "ServiceConfiguration": record.get("ServiceConfiguration", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
