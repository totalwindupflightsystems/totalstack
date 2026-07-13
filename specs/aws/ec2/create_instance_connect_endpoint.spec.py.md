---
id: "@specs/aws/ec2/create_instance_connect_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateInstanceConnectEndpoint"
---

# CreateInstanceConnectEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_instance_connect_endpoint
> **spec:implements:** @kind:operation CreateInstanceConnectEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateInstanceConnectEndpoint.spec.md

Creates an EC2 Instance Connect Endpoint. An EC2 Instance Connect Endpoint allows you to connect to an instance, without requiring the instance to have a public IPv4 or public IPv6 address. For more information, see Connect to your instances using EC2 Instance Connect Endpoint in the Amazon EC2 User Guide .

## Input Shape: CreateInstanceConnectEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| IpAddressType | Any  # complex shape |  | The IP address type of the endpoint. If no value is specified, the default value is determined by the IP address type of |
| PreserveClientIp | bool |  | Indicates whether the client IP address is preserved as the source. The following are the possible values. true - Use th |
| SecurityGroupIds | Any  # complex shape |  | One or more security groups to associate with the endpoint. If you don't specify a security group, the default security  |
| SubnetId | Any  # complex shape | ✓ | The ID of the subnet in which to create the EC2 Instance Connect Endpoint. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the EC2 Instance Connect Endpoint during creation. |

## Output Shape: CreateInstanceConnectEndpointResult

- **ClientToken** (str): Unique, case-sensitive idempotency token provided by the client in the the request.
- **InstanceConnectEndpoint** (Any  # complex shape): Information about the EC2 Instance Connect Endpoint.

## Implementation

```speclang
def create_instance_connect_endpoint(store, request: dict) -> dict:
    """Creates an EC2 Instance Connect Endpoint. An EC2 Instance Connect Endpoint allows you to connect to an instance, without requiring the instance to have a public IPv4 or public IPv6 address. For more i"""
    subnet_id = request.get("SubnetId", "").strip() if isinstance(request.get("SubnetId"), str) else request.get("SubnetId")
    if not subnet_id:
        raise ValidationException("SubnetId is required")

    if store.instance_connect_endpoints(subnet_id):
        raise ResourceInUseException(f"Resource subnet_id already exists")

    record = {
        "DryRun": dry_run,
        "SubnetId": subnet_id,
        "SecurityGroupIds": security_group_ids,
        "PreserveClientIp": preserve_client_ip,
        "ClientToken": client_token,
        "TagSpecifications": tag_specifications,
        "IpAddressType": ip_address_type,
    }

    store.instance_connect_endpoints(subnet_id, record)

    return {
        "InstanceConnectEndpoint": record.get("InstanceConnectEndpoint", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
