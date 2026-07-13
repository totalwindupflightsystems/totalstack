---
id: "@specs/aws/ec2/delete_vpc_endpoints"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVpcEndpoints"
---

# DeleteVpcEndpoints

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_vpc_endpoints
> **spec:implements:** @kind:operation DeleteVpcEndpoints
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVpcEndpoints.spec.md

Deletes the specified VPC endpoints. When you delete a gateway endpoint, we delete the endpoint routes in the route tables for the endpoint. When you delete a Gateway Load Balancer endpoint, we delete its endpoint network interfaces. You can only delete Gateway Load Balancer endpoints when the routes that are associated with the endpoint are deleted. When you delete an interface endpoint, we delete its endpoint network interfaces.

## Input Shape: DeleteVpcEndpointsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpcEndpointIds | list[Any  # complex shape] | ✓ | The IDs of the VPC endpoints. |

## Output Shape: DeleteVpcEndpointsResult

- **Unsuccessful** (Any  # complex shape): Information about the VPC endpoints that were not successfully deleted.

## Implementation

```speclang
def delete_vpc_endpoints(store, request: dict) -> dict:
    """Deletes the specified VPC endpoints. When you delete a gateway endpoint, we delete the endpoint routes in the route tables for the endpoint. When you delete a Gateway Load Balancer endpoint, we delete"""
    vpc_endpoint_ids = request.get("VpcEndpointIds", "").strip() if isinstance(request.get("VpcEndpointIds"), str) else request.get("VpcEndpointIds")

    if not store.vpc_endpointss(vpc_endpoint_ids):
        raise ResourceNotFoundException(f"Resource vpc_endpoint_ids not found")
    store.delete_vpc_endpointss(vpc_endpoint_ids)
    return {}
```
