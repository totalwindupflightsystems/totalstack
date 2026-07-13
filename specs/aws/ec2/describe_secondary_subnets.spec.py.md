---
id: "@specs/aws/ec2/describe_secondary_subnets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSecondarySubnets"
---

# DescribeSecondarySubnets

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_secondary_subnets
> **spec:implements:** @kind:operation DescribeSecondarySubnets
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSecondarySubnets.spec.md

Describes one or more of your secondary subnets.

## Input Shape: DescribeSecondarySubnetsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. ipv4-cidr-block-association.association-id - The association ID for an IPv4 CIDR block associated with the  |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| SecondarySubnetIds | list[Any  # complex shape] |  | The IDs of the secondary subnets. |

## Output Shape: DescribeSecondarySubnetsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **SecondarySubnets** (list[Any  # complex shape]): Information about the secondary subnets.

## Implementation

```speclang
def describe_secondary_subnets(store, request: dict) -> dict:
    """Describes one or more of your secondary subnets."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
