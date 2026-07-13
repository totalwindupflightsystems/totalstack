---
id: "@specs/aws/ec2/get_verified_access_endpoint_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetVerifiedAccessEndpointPolicy"
---

# GetVerifiedAccessEndpointPolicy

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_verified_access_endpoint_policy
> **spec:implements:** @kind:operation GetVerifiedAccessEndpointPolicy
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetVerifiedAccessEndpointPolicy.spec.md

Get the Verified Access policy associated with the endpoint.

## Input Shape: GetVerifiedAccessEndpointPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VerifiedAccessEndpointId | Any  # complex shape | ✓ | The ID of the Verified Access endpoint. |

## Output Shape: GetVerifiedAccessEndpointPolicyResult

- **PolicyDocument** (str): The Verified Access policy document.
- **PolicyEnabled** (bool): The status of the Verified Access policy.

## Implementation

```speclang
def get_verified_access_endpoint_policy(store, request: dict) -> dict:
    """Get the Verified Access policy associated with the endpoint."""
    verified_access_endpoint_id = request.get("VerifiedAccessEndpointId", "").strip() if isinstance(request.get("VerifiedAccessEndpointId"), str) else request.get("VerifiedAccessEndpointId")
    if not verified_access_endpoint_id:
        raise ValidationException("VerifiedAccessEndpointId is required")

    resource = store.verified_access_endpoint_policys(verified_access_endpoint_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource verified_access_endpoint_id not found")
    return {"VerifiedAccessEndpointId": verified_access_endpoint_id, **resource}
```
