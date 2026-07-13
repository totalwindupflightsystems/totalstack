---
id: "@specs/aws/ec2/modify_instance_connect_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyInstanceConnectEndpoint"
---

# ModifyInstanceConnectEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_instance_connect_endpoint
> **spec:implements:** @kind:operation ModifyInstanceConnectEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyInstanceConnectEndpoint.spec.md

Modifies the specified EC2 Instance Connect Endpoint. For more information, see Modify an EC2 Instance Connect Endpoint in the Amazon EC2 User Guide .

## Input Shape: ModifyInstanceConnectEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceConnectEndpointId | Any  # complex shape | ✓ | The ID of the EC2 Instance Connect Endpoint to modify. |
| IpAddressType | Any  # complex shape |  | The new IP address type for the EC2 Instance Connect Endpoint. PreserveClientIp is only supported on IPv4 EC2 Instance C |
| PreserveClientIp | bool |  | Indicates whether the client IP address is preserved as the source when you connect to a resource. The following are the |
| SecurityGroupIds | Any  # complex shape |  | Changes the security groups for the EC2 Instance Connect Endpoint. The new set of groups you specify replaces the curren |

## Output Shape: ModifyInstanceConnectEndpointResult

- **Return** (bool): Is true if the request succeeds and an error otherwise.

## Implementation

```speclang
def modify_instance_connect_endpoint(store, request: dict) -> dict:
    """Modifies the specified EC2 Instance Connect Endpoint. For more information, see Modify an EC2 Instance Connect Endpoint in the Amazon EC2 User Guide ."""
    instance_connect_endpoint_id = request.get("InstanceConnectEndpointId", "").strip() if isinstance(request.get("InstanceConnectEndpointId"), str) else request.get("InstanceConnectEndpointId")
    if not instance_connect_endpoint_id:
        raise ValidationException("InstanceConnectEndpointId is required")

    resource = store.instance_connect_endpoints(instance_connect_endpoint_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_connect_endpoint_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "IpAddressType" in request:
        resource["IpAddressType"] = ip_address_type
    if "SecurityGroupIds" in request:
        resource["SecurityGroupIds"] = security_group_ids
    if "PreserveClientIp" in request:
        resource["PreserveClientIp"] = preserve_client_ip

    store.instance_connect_endpoints(instance_connect_endpoint_id, resource)
    return resource
```
