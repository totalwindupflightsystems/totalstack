---
id: "@specs/aws/ec2/create_verified_access_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVerifiedAccessGroup"
---

# CreateVerifiedAccessGroup

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_verified_access_group
> **spec:implements:** @kind:operation CreateVerifiedAccessGroup
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVerifiedAccessGroup.spec.md

An Amazon Web Services Verified Access group is a collection of Amazon Web Services Verified Access endpoints who's associated applications have similar security requirements. Each instance within a Verified Access group shares an Verified Access policy. For example, you can group all Verified Access instances associated with "sales" applications together and use one common Verified Access policy.

## Input Shape: CreateVerifiedAccessGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| Description | str |  | A description for the Verified Access group. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PolicyDocument | str |  | The Verified Access policy document. |
| SseSpecification | Any  # complex shape |  | The options for server side encryption. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the Verified Access group. |
| VerifiedAccessInstanceId | Any  # complex shape | ✓ | The ID of the Verified Access instance. |

## Output Shape: CreateVerifiedAccessGroupResult

- **VerifiedAccessGroup** (Any  # complex shape): Details about the Verified Access group.

## Implementation

```speclang
def create_verified_access_group(store, request: dict) -> dict:
    """An Amazon Web Services Verified Access group is a collection of Amazon Web Services Verified Access endpoints who's associated applications have similar security requirements. Each instance within a V"""
    verified_access_instance_id = request.get("VerifiedAccessInstanceId", "").strip() if isinstance(request.get("VerifiedAccessInstanceId"), str) else request.get("VerifiedAccessInstanceId")
    if not verified_access_instance_id:
        raise ValidationException("VerifiedAccessInstanceId is required")

    if store.verified_access_groups(verified_access_instance_id):
        raise ResourceInUseException(f"Resource verified_access_instance_id already exists")

    record = {
        "VerifiedAccessInstanceId": verified_access_instance_id,
        "Description": description,
        "PolicyDocument": policy_document,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
        "DryRun": dry_run,
        "SseSpecification": sse_specification,
    }

    store.verified_access_groups(verified_access_instance_id, record)

    return {
        "VerifiedAccessGroup": record.get("VerifiedAccessGroup", {}),
    }
```
