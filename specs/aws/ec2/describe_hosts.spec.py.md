---
id: "@specs/aws/ec2/describe_hosts"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeHosts"
---

# DescribeHosts

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_hosts
> **spec:implements:** @kind:operation DescribeHosts
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeHosts.spec.md

Describes the specified Dedicated Hosts or all your Dedicated Hosts. The results describe only the Dedicated Hosts in the Region you're currently using. All listed instances consume capacity on your Dedicated Host. Dedicated Hosts that have recently been released are listed with the state released .

## Input Shape: DescribeHostsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Filter | list[Any  # complex shape] |  | The filters. auto-placement - Whether auto-placement is enabled or disabled ( on | off ). availability-zone - The Availa |
| HostIds | list[Any  # complex shape] |  | The IDs of the Dedicated Hosts. The IDs are used for targeted instance launches. |
| MaxResults | int |  | The maximum number of results to return for the request in a single page. The remaining results can be seen by sending a |
| NextToken | str |  | The token to use to retrieve the next page of results. |

## Output Shape: DescribeHostsResult

- **Hosts** (list[Any  # complex shape]): Information about the Dedicated Hosts.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_hosts(store, request: dict) -> dict:
    """Describes the specified Dedicated Hosts or all your Dedicated Hosts. The results describe only the Dedicated Hosts in the Region you're currently using. All listed instances consume capacity on your D"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
