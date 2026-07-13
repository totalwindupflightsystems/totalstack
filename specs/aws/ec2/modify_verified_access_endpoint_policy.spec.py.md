---
id: "@specs/aws/ec2/modify_verified_access_endpoint_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVerifiedAccessEndpointPolicy"
---

# ModifyVerifiedAccessEndpointPolicy

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_verified_access_endpoint_policy
> **spec:implements:** @kind:operation ModifyVerifiedAccessEndpointPolicy
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVerifiedAccessEndpointPolicy.spec.md

Modifies the specified Amazon Web Services Verified Access endpoint policy.

## Input Shape: ModifyVerifiedAccessEndpointPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PolicyDocument | str |  | The Verified Access policy document. |
| PolicyEnabled | bool |  | The status of the Verified Access policy. |
| SseSpecification | Any  # complex shape |  | The options for server side encryption. |
| VerifiedAccessEndpointId | Any  # complex shape | ✓ | The ID of the Verified Access endpoint. |

## Output Shape: ModifyVerifiedAccessEndpointPolicyResult

- **PolicyDocument** (str): The Verified Access policy document.
- **PolicyEnabled** (bool): The status of the Verified Access policy.
- **SseSpecification** (Any  # complex shape): The options in use for server side encryption.

## Implementation

```speclang
def modify_verified_access_endpoint_policy(store, request: dict) -> dict:
    """Modifies the specified Amazon Web Services Verified Access endpoint policy."""
    verified_access_endpoint_id = request.get("VerifiedAccessEndpointId", "").strip() if isinstance(request.get("VerifiedAccessEndpointId"), str) else request.get("VerifiedAccessEndpointId")
    if not verified_access_endpoint_id:
        raise ValidationException("VerifiedAccessEndpointId is required")

    resource = store.verified_access_endpoint_policys(verified_access_endpoint_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource verified_access_endpoint_id not found")

    # Update mutable fields
    if "PolicyEnabled" in request:
        resource["PolicyEnabled"] = policy_enabled
    if "PolicyDocument" in request:
        resource["PolicyDocument"] = policy_document
    if "ClientToken" in request:
        resource["ClientToken"] = client_token
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "SseSpecification" in request:
        resource["SseSpecification"] = sse_specification

    store.verified_access_endpoint_policys(verified_access_endpoint_id, resource)
    return resource
```
