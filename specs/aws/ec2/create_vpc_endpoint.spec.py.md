---
id: "@specs/aws/ec2/create_vpc_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVpcEndpoint"
---

# CreateVpcEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_vpc_endpoint
> **spec:implements:** @kind:operation CreateVpcEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVpcEndpoint.spec.md

Creates a VPC endpoint. A VPC endpoint provides a private connection between the specified VPC and the specified endpoint service. You can use an endpoint service provided by Amazon Web Services, an Amazon Web Services Marketplace Partner, or another Amazon Web Services account. For more information, see the Amazon Web Services PrivateLink User Guide .

## Input Shape: CreateVpcEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| DnsOptions | Any  # complex shape |  | The DNS options for the endpoint. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| IpAddressType | Any  # complex shape |  | The IP address type for the endpoint. |
| PolicyDocument | str |  | (Interface and gateway endpoints) A policy to attach to the endpoint that controls access to the service. The policy mus |
| PrivateDnsEnabled | bool |  | (Interface endpoint) Indicates whether to associate a private hosted zone with the specified VPC. The private hosted zon |
| ResourceConfigurationArn | Any  # complex shape |  | The Amazon Resource Name (ARN) of a resource configuration that will be associated with the VPC endpoint of type resourc |
| RouteTableIds | list[Any  # complex shape] |  | (Gateway endpoint) The route table IDs. |
| SecurityGroupIds | list[Any  # complex shape] |  | (Interface endpoint) The IDs of the security groups to associate with the endpoint network interfaces. If this parameter |
| ServiceName | str |  | The name of the endpoint service. |
| ServiceNetworkArn | Any  # complex shape |  | The Amazon Resource Name (ARN) of a service network that will be associated with the VPC endpoint of type service-networ |
| ServiceRegion | str |  | The Region where the service is hosted. The default is the current Region. |
| SubnetConfigurations | list[Any  # complex shape] |  | The subnet configurations for the endpoint. |
| SubnetIds | list[Any  # complex shape] |  | (Interface and Gateway Load Balancer endpoints) The IDs of the subnets in which to create endpoint network interfaces. F |
| TagSpecifications | list[Any  # complex shape] |  | The tags to associate with the endpoint. |
| VpcEndpointType | Any  # complex shape |  | The type of endpoint. Default: Gateway |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Output Shape: CreateVpcEndpointResult

- **ClientToken** (str): Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
- **VpcEndpoint** (Any  # complex shape): Information about the endpoint.

## Implementation

```speclang
def create_vpc_endpoint(store, request: dict) -> dict:
    """Creates a VPC endpoint. A VPC endpoint provides a private connection between the specified VPC and the specified endpoint service. You can use an endpoint service provided by Amazon Web Services, an A"""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    if store.vpc_endpoints(vpc_id):
        raise ResourceInUseException(f"Resource vpc_id already exists")

    record = {
        "DryRun": dry_run,
        "VpcEndpointType": vpc_endpoint_type,
        "VpcId": vpc_id,
        "ServiceName": service_name,
        "PolicyDocument": policy_document,
        "RouteTableIds": route_table_ids,
        "SubnetIds": subnet_ids,
        "SecurityGroupIds": security_group_ids,
        "IpAddressType": ip_address_type,
        "DnsOptions": dns_options,
        "ClientToken": client_token,
        "PrivateDnsEnabled": private_dns_enabled,
        "TagSpecifications": tag_specifications,
        "SubnetConfigurations": subnet_configurations,
        "ServiceNetworkArn": service_network_arn,
        "ResourceConfigurationArn": resource_configuration_arn,
        "ServiceRegion": service_region,
    }

    store.vpc_endpoints(vpc_id, record)

    return {
        "VpcEndpoint": record.get("VpcEndpoint", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
