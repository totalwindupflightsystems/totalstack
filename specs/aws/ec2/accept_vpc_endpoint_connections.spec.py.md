---
id: "@specs/aws/ec2/accept_vpc_endpoint_connections"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AcceptVpcEndpointConnections"
---

# AcceptVpcEndpointConnections

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/accept_vpc_endpoint_connections
> **spec:implements:** @kind:operation AcceptVpcEndpointConnections
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AcceptVpcEndpointConnections.spec.md

Accepts connection requests to your VPC endpoint service.

## Input Shape: AcceptVpcEndpointConnectionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ServiceId | Any  # complex shape | ✓ | The ID of the VPC endpoint service. |
| VpcEndpointIds | list[Any  # complex shape] | ✓ | The IDs of the interface VPC endpoints. |

## Output Shape: AcceptVpcEndpointConnectionsResult

- **Unsuccessful** (Any  # complex shape): Information about the interface endpoints that were not accepted, if applicable.

## Implementation

```speclang
def accept_vpc_endpoint_connections(store, request: dict) -> dict:
    """Accepts connection requests to your VPC endpoint service."""
    service_id = request.get("ServiceId", "").strip() if isinstance(request.get("ServiceId"), str) else request.get("ServiceId")
    if not service_id:
        raise ValidationException("ServiceId is required")
    vpc_endpoint_ids = request.get("VpcEndpointIds", "").strip() if isinstance(request.get("VpcEndpointIds"), str) else request.get("VpcEndpointIds")
    if not vpc_endpoint_ids:
        raise ValidationException("VpcEndpointIds is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AcceptVpcEndpointConnections", request)
```
