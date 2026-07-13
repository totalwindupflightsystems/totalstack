---
id: "@specs/aws/ec2/describe_secondary_networks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSecondaryNetworks"
---

# DescribeSecondaryNetworks

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_secondary_networks
> **spec:implements:** @kind:operation DescribeSecondaryNetworks
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSecondaryNetworks.spec.md

Describes one or more secondary networks.

## Input Shape: DescribeSecondaryNetworksRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. The following are the possible values: ipv4-cidr-block-association.association-id - The association ID for  |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| SecondaryNetworkIds | list[Any  # complex shape] |  | The IDs of the secondary networks. |

## Output Shape: DescribeSecondaryNetworksResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **SecondaryNetworks** (list[Any  # complex shape]): Information about the secondary networks.

## Implementation

```speclang
def describe_secondary_networks(store, request: dict) -> dict:
    """Describes one or more secondary networks."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
