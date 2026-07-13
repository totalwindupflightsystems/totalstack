---
id: "@specs/aws/ec2/modify_vpc_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpcEndpoint"
---

# ModifyVpcEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpc_endpoint
> **spec:implements:** @kind:operation ModifyVpcEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpcEndpoint.spec.md

Modifies attributes of a specified VPC endpoint. The attributes that you can modify depend on the type of VPC endpoint (interface, gateway, or Gateway Load Balancer). For more information, see the Amazon Web Services PrivateLink Guide .

## Input Shape: ModifyVpcEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddRouteTableIds | list[Any  # complex shape] |  | (Gateway endpoint) The IDs of the route tables to associate with the endpoint. |
| AddSecurityGroupIds | list[Any  # complex shape] |  | (Interface endpoint) The IDs of the security groups to associate with the endpoint network interfaces. |
| AddSubnetIds | list[Any  # complex shape] |  | (Interface and Gateway Load Balancer endpoints) The IDs of the subnets in which to serve the endpoint. For a Gateway Loa |
| DnsOptions | Any  # complex shape |  | The DNS options for the endpoint. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| IpAddressType | Any  # complex shape |  | The IP address type for the endpoint. |
| PolicyDocument | str |  | (Interface and gateway endpoints) A policy to attach to the endpoint that controls access to the service. The policy mus |
| PrivateDnsEnabled | bool |  | (Interface endpoint) Indicates whether a private hosted zone is associated with the VPC. |
| RemoveRouteTableIds | list[Any  # complex shape] |  | (Gateway endpoint) The IDs of the route tables to disassociate from the endpoint. |
| RemoveSecurityGroupIds | list[Any  # complex shape] |  | (Interface endpoint) The IDs of the security groups to disassociate from the endpoint network interfaces. |
| RemoveSubnetIds | list[Any  # complex shape] |  | (Interface endpoint) The IDs of the subnets from which to remove the endpoint. |
| ResetPolicy | bool |  | (Gateway endpoint) Specify true to reset the policy document to the default policy. The default policy allows full acces |
| SubnetConfigurations | list[Any  # complex shape] |  | The subnet configurations for the endpoint. |
| VpcEndpointId | Any  # complex shape | ✓ | The ID of the endpoint. |

## Output Shape: ModifyVpcEndpointResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def modify_vpc_endpoint(store, request: dict) -> dict:
    """Modifies attributes of a specified VPC endpoint. The attributes that you can modify depend on the type of VPC endpoint (interface, gateway, or Gateway Load Balancer). For more information, see the Ama"""
    vpc_endpoint_id = request.get("VpcEndpointId", "").strip() if isinstance(request.get("VpcEndpointId"), str) else request.get("VpcEndpointId")
    if not vpc_endpoint_id:
        raise ValidationException("VpcEndpointId is required")

    resource = store.vpc_endpoints(vpc_endpoint_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpc_endpoint_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "ResetPolicy" in request:
        resource["ResetPolicy"] = reset_policy
    if "PolicyDocument" in request:
        resource["PolicyDocument"] = policy_document
    if "AddRouteTableIds" in request:
        resource["AddRouteTableIds"] = add_route_table_ids
    if "RemoveRouteTableIds" in request:
        resource["RemoveRouteTableIds"] = remove_route_table_ids
    if "AddSubnetIds" in request:
        resource["AddSubnetIds"] = add_subnet_ids
    if "RemoveSubnetIds" in request:
        resource["RemoveSubnetIds"] = remove_subnet_ids
    if "AddSecurityGroupIds" in request:
        resource["AddSecurityGroupIds"] = add_security_group_ids
    if "RemoveSecurityGroupIds" in request:
        resource["RemoveSecurityGroupIds"] = remove_security_group_ids
    if "IpAddressType" in request:
        resource["IpAddressType"] = ip_address_type
    if "DnsOptions" in request:
        resource["DnsOptions"] = dns_options
    if "PrivateDnsEnabled" in request:
        resource["PrivateDnsEnabled"] = private_dns_enabled
    if "SubnetConfigurations" in request:
        resource["SubnetConfigurations"] = subnet_configurations

    store.vpc_endpoints(vpc_endpoint_id, resource)
    return resource
```
