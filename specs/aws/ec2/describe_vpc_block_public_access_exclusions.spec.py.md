---
id: "@specs/aws/ec2/describe_vpc_block_public_access_exclusions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcBlockPublicAccessExclusions"
---

# DescribeVpcBlockPublicAccessExclusions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_block_public_access_exclusions
> **spec:implements:** @kind:operation DescribeVpcBlockPublicAccessExclusions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcBlockPublicAccessExclusions.spec.md

Describe VPC Block Public Access (BPA) exclusions. A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s BPA mode and will allow bidirectional or egress-only access. You can create BPA exclusions for VPCs and subnets even when BPA is not enabled on the account to ensure that there is no traffic disruption to the exclusions when VPC BPA is turned on. To learn more about VPC BPA, see Block public access to VPCs and subnets in the Amazon VPC User Guide .

## Input Shape: DescribeVpcBlockPublicAccessExclusionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ExclusionIds | list[Any  # complex shape] |  | IDs of exclusions. |
| Filters | list[Any  # complex shape] |  | Filters for the request: resource-arn - The Amazon Resource Name (ARN) of a exclusion. internet-gateway-exclusion-mode - |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeVpcBlockPublicAccessExclusionsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **VpcBlockPublicAccessExclusions** (list[Any  # complex shape]): Details related to the exclusions.

## Implementation

```speclang
def describe_vpc_block_public_access_exclusions(store, request: dict) -> dict:
    """Describe VPC Block Public Access (BPA) exclusions. A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s BPA mode and will allow bidirectional """

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
