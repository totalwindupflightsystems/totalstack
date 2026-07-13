---
id: "@specs/aws/ec2/get_verified_access_endpoint_targets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetVerifiedAccessEndpointTargets"
---

# GetVerifiedAccessEndpointTargets

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_verified_access_endpoint_targets
> **spec:implements:** @kind:operation GetVerifiedAccessEndpointTargets
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetVerifiedAccessEndpointTargets.spec.md

Gets the targets for the specified network CIDR endpoint for Verified Access.

## Input Shape: GetVerifiedAccessEndpointTargetsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| VerifiedAccessEndpointId | Any  # complex shape | ✓ | The ID of the network CIDR endpoint. |

## Output Shape: GetVerifiedAccessEndpointTargetsResult

- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **VerifiedAccessEndpointTargets** (list[Any  # complex shape]): The Verified Access targets.

## Implementation

```speclang
def get_verified_access_endpoint_targets(store, request: dict) -> dict:
    """Gets the targets for the specified network CIDR endpoint for Verified Access."""
    verified_access_endpoint_id = request.get("VerifiedAccessEndpointId", "").strip() if isinstance(request.get("VerifiedAccessEndpointId"), str) else request.get("VerifiedAccessEndpointId")
    if not verified_access_endpoint_id:
        raise ValidationException("VerifiedAccessEndpointId is required")

    resource = store.verified_access_endpoint_targetss(verified_access_endpoint_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource verified_access_endpoint_id not found")
    return {"VerifiedAccessEndpointId": verified_access_endpoint_id, **resource}
```
