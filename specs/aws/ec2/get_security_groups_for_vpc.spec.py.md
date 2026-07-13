---
id: "@specs/aws/ec2/get_security_groups_for_vpc"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetSecurityGroupsForVpc"
---

# GetSecurityGroupsForVpc

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_security_groups_for_vpc
> **spec:implements:** @kind:operation GetSecurityGroupsForVpc
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetSecurityGroupsForVpc.spec.md

Gets security groups that can be associated by the Amazon Web Services account making the request with network interfaces in the specified VPC.

## Input Shape: GetSecurityGroupsForVpcRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. If using multiple filters, the results include security groups which match all filters. group-id : The secu |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| VpcId | Any  # complex shape | ✓ | The VPC ID where the security group can be used. |

## Output Shape: GetSecurityGroupsForVpcResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **SecurityGroupForVpcs** (list[Any  # complex shape]): The security group that can be used by interfaces in the VPC.

## Implementation

```speclang
def get_security_groups_for_vpc(store, request: dict) -> dict:
    """Gets security groups that can be associated by the Amazon Web Services account making the request with network interfaces in the specified VPC."""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    resource = store.security_groups_for_vpcs(vpc_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpc_id not found")
    return {"VpcId": vpc_id, **resource}
```
