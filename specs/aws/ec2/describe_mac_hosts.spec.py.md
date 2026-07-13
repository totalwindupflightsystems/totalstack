---
id: "@specs/aws/ec2/describe_mac_hosts"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeMacHosts"
---

# DescribeMacHosts

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_mac_hosts
> **spec:implements:** @kind:operation DescribeMacHosts
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeMacHosts.spec.md

Describes the specified EC2 Mac Dedicated Host or all of your EC2 Mac Dedicated Hosts.

## Input Shape: DescribeMacHostsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Filters | list[Any  # complex shape] |  | The filters. availability-zone - The Availability Zone of the EC2 Mac Dedicated Host. instance-type - The instance type  |
| HostIds | list[Any  # complex shape] |  | The IDs of the EC2 Mac Dedicated Hosts. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return for the request in a single page. The remaining results can be seen by sending a |
| NextToken | str |  | The token to use to retrieve the next page of results. |

## Output Shape: DescribeMacHostsResult

- **MacHosts** (list[Any  # complex shape]): Information about the EC2 Mac Dedicated Hosts.
- **NextToken** (str): The token to use to retrieve the next page of results.

## Implementation

```speclang
def describe_mac_hosts(store, request: dict) -> dict:
    """Describes the specified EC2 Mac Dedicated Host or all of your EC2 Mac Dedicated Hosts."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
