---
id: "@specs/aws/ec2/describe_stale_security_groups"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeStaleSecurityGroups"
---

# DescribeStaleSecurityGroups

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_stale_security_groups
> **spec:implements:** @kind:operation DescribeStaleSecurityGroups
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeStaleSecurityGroups.spec.md

Describes the stale security group rules for security groups referenced across a VPC peering connection, transit gateway connection, or with a security group VPC association. Rules are stale when they reference a deleted security group. Rules can also be stale if they reference a security group in a peer VPC for which the VPC peering connection has been deleted, across a transit gateway where the transit gateway has been deleted (or the transit gateway security group referencing feature has been disabled), or if a security group VPC association has been disassociated.

## Input Shape: DescribeStaleSecurityGroupsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Output Shape: DescribeStaleSecurityGroupsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **StaleSecurityGroupSet** (Any  # complex shape): Information about the stale security groups.

## Implementation

```speclang
def describe_stale_security_groups(store, request: dict) -> dict:
    """Describes the stale security group rules for security groups referenced across a VPC peering connection, transit gateway connection, or with a security group VPC association. Rules are stale when they"""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    resource = store.stale_security_groupss(vpc_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpc_id not found")
    return {"VpcId": vpc_id, **resource}
```
