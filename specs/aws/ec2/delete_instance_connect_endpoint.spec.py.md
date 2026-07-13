---
id: "@specs/aws/ec2/delete_instance_connect_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteInstanceConnectEndpoint"
---

# DeleteInstanceConnectEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_instance_connect_endpoint
> **spec:implements:** @kind:operation DeleteInstanceConnectEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteInstanceConnectEndpoint.spec.md

Deletes the specified EC2 Instance Connect Endpoint.

## Input Shape: DeleteInstanceConnectEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceConnectEndpointId | Any  # complex shape | ✓ | The ID of the EC2 Instance Connect Endpoint to delete. |

## Output Shape: DeleteInstanceConnectEndpointResult

- **InstanceConnectEndpoint** (Any  # complex shape): Information about the EC2 Instance Connect Endpoint.

## Implementation

```speclang
def delete_instance_connect_endpoint(store, request: dict) -> dict:
    """Deletes the specified EC2 Instance Connect Endpoint."""
    instance_connect_endpoint_id = request.get("InstanceConnectEndpointId", "").strip() if isinstance(request.get("InstanceConnectEndpointId"), str) else request.get("InstanceConnectEndpointId")

    if not store.instance_connect_endpoints(instance_connect_endpoint_id):
        raise ResourceNotFoundException(f"Resource instance_connect_endpoint_id not found")
    store.delete_instance_connect_endpoints(instance_connect_endpoint_id)
    return {}
```
