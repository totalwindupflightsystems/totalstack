---
id: "@specs/aws/ec2/delete_verified_access_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVerifiedAccessEndpoint"
---

# DeleteVerifiedAccessEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_verified_access_endpoint
> **spec:implements:** @kind:operation DeleteVerifiedAccessEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVerifiedAccessEndpoint.spec.md

Delete an Amazon Web Services Verified Access endpoint.

## Input Shape: DeleteVerifiedAccessEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VerifiedAccessEndpointId | Any  # complex shape | ✓ | The ID of the Verified Access endpoint. |

## Output Shape: DeleteVerifiedAccessEndpointResult

- **VerifiedAccessEndpoint** (Any  # complex shape): Details about the Verified Access endpoint.

## Implementation

```speclang
def delete_verified_access_endpoint(store, request: dict) -> dict:
    """Delete an Amazon Web Services Verified Access endpoint."""
    verified_access_endpoint_id = request.get("VerifiedAccessEndpointId", "").strip() if isinstance(request.get("VerifiedAccessEndpointId"), str) else request.get("VerifiedAccessEndpointId")

    if not store.verified_access_endpoints(verified_access_endpoint_id):
        raise ResourceNotFoundException(f"Resource verified_access_endpoint_id not found")
    store.delete_verified_access_endpoints(verified_access_endpoint_id)
    return {}
```
