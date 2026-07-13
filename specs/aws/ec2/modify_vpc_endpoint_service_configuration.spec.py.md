---
id: "@specs/aws/ec2/modify_vpc_endpoint_service_configuration"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpcEndpointServiceConfiguration"
---

# ModifyVpcEndpointServiceConfiguration

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpc_endpoint_service_configuration
> **spec:implements:** @kind:operation ModifyVpcEndpointServiceConfiguration
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpcEndpointServiceConfiguration.spec.md

Modifies the attributes of the specified VPC endpoint service configuration. If you set or modify the private DNS name, you must prove that you own the private DNS domain name.

## Input Shape: ModifyVpcEndpointServiceConfigurationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AcceptanceRequired | bool |  | Indicates whether requests to create an endpoint to the service must be accepted. |
| AddGatewayLoadBalancerArns | list[str] |  | The Amazon Resource Names (ARNs) of Gateway Load Balancers to add to the service configuration. |
| AddNetworkLoadBalancerArns | list[str] |  | The Amazon Resource Names (ARNs) of Network Load Balancers to add to the service configuration. |
| AddSupportedIpAddressTypes | list[str] |  | The IP address types to add to the service configuration. |
| AddSupportedRegions | list[str] |  | The supported Regions to add to the service configuration. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PrivateDnsName | str |  | (Interface endpoint configuration) The private DNS name to assign to the endpoint service. |
| RemoveGatewayLoadBalancerArns | list[str] |  | The Amazon Resource Names (ARNs) of Gateway Load Balancers to remove from the service configuration. |
| RemoveNetworkLoadBalancerArns | list[str] |  | The Amazon Resource Names (ARNs) of Network Load Balancers to remove from the service configuration. |
| RemovePrivateDnsName | bool |  | (Interface endpoint configuration) Removes the private DNS name of the endpoint service. |
| RemoveSupportedIpAddressTypes | list[str] |  | The IP address types to remove from the service configuration. |
| RemoveSupportedRegions | list[str] |  | The supported Regions to remove from the service configuration. |
| ServiceId | Any  # complex shape | ✓ | The ID of the service. |

## Output Shape: ModifyVpcEndpointServiceConfigurationResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def modify_vpc_endpoint_service_configuration(store, request: dict) -> dict:
    """Modifies the attributes of the specified VPC endpoint service configuration. If you set or modify the private DNS name, you must prove that you own the private DNS domain name."""
    service_id = request.get("ServiceId", "").strip() if isinstance(request.get("ServiceId"), str) else request.get("ServiceId")
    if not service_id:
        raise ValidationException("ServiceId is required")

    resource = store.vpc_endpoint_service_configurations(service_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource service_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "PrivateDnsName" in request:
        resource["PrivateDnsName"] = private_dns_name
    if "RemovePrivateDnsName" in request:
        resource["RemovePrivateDnsName"] = remove_private_dns_name
    if "AcceptanceRequired" in request:
        resource["AcceptanceRequired"] = acceptance_required
    if "AddNetworkLoadBalancerArns" in request:
        resource["AddNetworkLoadBalancerArns"] = add_network_load_balancer_arns
    if "RemoveNetworkLoadBalancerArns" in request:
        resource["RemoveNetworkLoadBalancerArns"] = remove_network_load_balancer_arns
    if "AddGatewayLoadBalancerArns" in request:
        resource["AddGatewayLoadBalancerArns"] = add_gateway_load_balancer_arns
    if "RemoveGatewayLoadBalancerArns" in request:
        resource["RemoveGatewayLoadBalancerArns"] = remove_gateway_load_balancer_arns
    if "AddSupportedIpAddressTypes" in request:
        resource["AddSupportedIpAddressTypes"] = add_supported_ip_address_types
    if "RemoveSupportedIpAddressTypes" in request:
        resource["RemoveSupportedIpAddressTypes"] = remove_supported_ip_address_types
    if "AddSupportedRegions" in request:
        resource["AddSupportedRegions"] = add_supported_regions
    if "RemoveSupportedRegions" in request:
        resource["RemoveSupportedRegions"] = remove_supported_regions

    store.vpc_endpoint_service_configurations(service_id, resource)
    return resource
```
