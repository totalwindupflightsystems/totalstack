---
id: "@specs/aws/ec2/cancel_spot_instance_requests"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CancelSpotInstanceRequests"
---

# CancelSpotInstanceRequests

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/cancel_spot_instance_requests
> **spec:implements:** @kind:operation CancelSpotInstanceRequests
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CancelSpotInstanceRequests.spec.md

Cancels one or more Spot Instance requests. Canceling a Spot Instance request does not terminate running Spot Instances associated with the request.

## Input Shape: CancelSpotInstanceRequestsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SpotInstanceRequestIds | list[Any  # complex shape] | ✓ | The IDs of the Spot Instance requests. |

## Output Shape: CancelSpotInstanceRequestsResult

- **CancelledSpotInstanceRequests** (list[Any  # complex shape]): The Spot Instance requests.

## Implementation

```speclang
def cancel_spot_instance_requests(store, request: dict) -> dict:
    """Cancels one or more Spot Instance requests. Canceling a Spot Instance request does not terminate running Spot Instances associated with the request."""
    spot_instance_request_ids = request.get("SpotInstanceRequestIds", "").strip() if isinstance(request.get("SpotInstanceRequestIds"), str) else request.get("SpotInstanceRequestIds")

    if not store.spot_instance_requestss(spot_instance_request_ids):
        raise ResourceNotFoundException(f"Resource spot_instance_request_ids not found")
    store.delete_spot_instance_requestss(spot_instance_request_ids)
    return {}
```
