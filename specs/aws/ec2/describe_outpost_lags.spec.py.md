---
id: "@specs/aws/ec2/describe_outpost_lags"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeOutpostLags"
---

# DescribeOutpostLags

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_outpost_lags
> **spec:implements:** @kind:operation DescribeOutpostLags
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeOutpostLags.spec.md

Describes the Outposts link aggregation groups (LAGs). LAGs are only available for second-generation Outposts racks at this time.

## Input Shape: DescribeOutpostLagsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters to use for narrowing down the request. The following filters are supported: service-link-virtual-interface-i |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| OutpostLagIds | Any  # complex shape |  | The IDs of the Outpost LAGs. |

## Output Shape: DescribeOutpostLagsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **OutpostLags** (Any  # complex shape): The Outpost LAGs.

## Implementation

```speclang
def describe_outpost_lags(store, request: dict) -> dict:
    """Describes the Outposts link aggregation groups (LAGs). LAGs are only available for second-generation Outposts racks at this time."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
