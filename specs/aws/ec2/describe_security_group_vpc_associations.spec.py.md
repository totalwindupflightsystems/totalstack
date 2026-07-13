---
id: "@specs/aws/ec2/describe_security_group_vpc_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSecurityGroupVpcAssociations"
---

# DescribeSecurityGroupVpcAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_security_group_vpc_associations
> **spec:implements:** @kind:operation DescribeSecurityGroupVpcAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSecurityGroupVpcAssociations.spec.md

Describes security group VPC associations made with AssociateSecurityGroupVpc .

## Input Shape: DescribeSecurityGroupVpcAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | Security group VPC association filters. group-id : The security group ID. group-owner-id : The group owner ID. state : T |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeSecurityGroupVpcAssociationsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **SecurityGroupVpcAssociations** (list[Any  # complex shape]): The security group VPC associations.

## Implementation

```speclang
def describe_security_group_vpc_associations(store, request: dict) -> dict:
    """Describes security group VPC associations made with AssociateSecurityGroupVpc ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
