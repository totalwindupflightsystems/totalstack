---
id: "@specs/aws/ec2/modify_verified_access_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVerifiedAccessEndpoint"
---

# ModifyVerifiedAccessEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_verified_access_endpoint
> **spec:implements:** @kind:operation ModifyVerifiedAccessEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVerifiedAccessEndpoint.spec.md

Modifies the configuration of the specified Amazon Web Services Verified Access endpoint.

## Input Shape: ModifyVerifiedAccessEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CidrOptions | Any  # complex shape |  | The CIDR options. |
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| Description | str |  | A description for the Verified Access endpoint. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LoadBalancerOptions | Any  # complex shape |  | The load balancer details if creating the Verified Access endpoint as load-balancer type. |
| NetworkInterfaceOptions | Any  # complex shape |  | The network interface options. |
| RdsOptions | Any  # complex shape |  | The RDS options. |
| VerifiedAccessEndpointId | Any  # complex shape | ✓ | The ID of the Verified Access endpoint. |
| VerifiedAccessGroupId | Any  # complex shape |  | The ID of the Verified Access group. |

## Output Shape: ModifyVerifiedAccessEndpointResult

- **VerifiedAccessEndpoint** (Any  # complex shape): Details about the Verified Access endpoint.

## Implementation

```speclang
def modify_verified_access_endpoint(store, request: dict) -> dict:
    """Modifies the configuration of the specified Amazon Web Services Verified Access endpoint."""
    verified_access_endpoint_id = request.get("VerifiedAccessEndpointId", "").strip() if isinstance(request.get("VerifiedAccessEndpointId"), str) else request.get("VerifiedAccessEndpointId")
    if not verified_access_endpoint_id:
        raise ValidationException("VerifiedAccessEndpointId is required")

    resource = store.verified_access_endpoints(verified_access_endpoint_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource verified_access_endpoint_id not found")

    # Update mutable fields
    if "VerifiedAccessGroupId" in request:
        resource["VerifiedAccessGroupId"] = verified_access_group_id
    if "LoadBalancerOptions" in request:
        resource["LoadBalancerOptions"] = load_balancer_options
    if "NetworkInterfaceOptions" in request:
        resource["NetworkInterfaceOptions"] = network_interface_options
    if "Description" in request:
        resource["Description"] = description
    if "ClientToken" in request:
        resource["ClientToken"] = client_token
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "RdsOptions" in request:
        resource["RdsOptions"] = rds_options
    if "CidrOptions" in request:
        resource["CidrOptions"] = cidr_options

    store.verified_access_endpoints(verified_access_endpoint_id, resource)
    return resource
```
