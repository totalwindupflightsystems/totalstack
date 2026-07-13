---
id: "@specs/aws/ec2/describe_ipams"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeIpams"
---

# DescribeIpams

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_ipams
> **spec:implements:** @kind:operation DescribeIpams
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeIpams.spec.md

Get information about your IPAM pools. For more information, see What is IPAM? in the Amazon VPC IPAM User Guide .

## Input Shape: DescribeIpamsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters for the request. For more information about filtering, see Filtering CLI output . |
| IpamIds | list[str] |  | The IDs of the IPAMs you want information on. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in the request. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeIpamsResult

- **Ipams** (Any  # complex shape): Information about the IPAMs.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_ipams(store, request: dict) -> dict:
    """Get information about your IPAM pools. For more information, see What is IPAM? in the Amazon VPC IPAM User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
