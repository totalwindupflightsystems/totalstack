---
id: "@specs/aws/ec2/describe_security_group_references"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSecurityGroupReferences"
---

# DescribeSecurityGroupReferences

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_security_group_references
> **spec:implements:** @kind:operation DescribeSecurityGroupReferences
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSecurityGroupReferences.spec.md

Describes the VPCs on the other side of a VPC peering or Transit Gateway connection that are referencing the security groups you've specified in this request.

## Input Shape: DescribeSecurityGroupReferencesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GroupId | Any  # complex shape | ✓ | The IDs of the security groups in your account. |

## Output Shape: DescribeSecurityGroupReferencesResult

- **SecurityGroupReferenceSet** (Any  # complex shape): Information about the VPCs with the referencing security groups.

## Implementation

```speclang
def describe_security_group_references(store, request: dict) -> dict:
    """Describes the VPCs on the other side of a VPC peering or Transit Gateway connection that are referencing the security groups you've specified in this request."""
    group_id = request.get("GroupId", "").strip() if isinstance(request.get("GroupId"), str) else request.get("GroupId")
    if not group_id:
        raise ValidationException("GroupId is required")

    resource = store.security_group_referencess(group_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource group_id not found")
    return {"GroupId": group_id, **resource}
```
