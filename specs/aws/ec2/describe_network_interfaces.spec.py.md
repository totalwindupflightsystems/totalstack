---
id: "@specs/aws/ec2/describe_network_interfaces"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeNetworkInterfaces"
---

# DescribeNetworkInterfaces

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_network_interfaces
> **spec:implements:** @kind:operation DescribeNetworkInterfaces
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeNetworkInterfaces.spec.md

Describes the specified network interfaces or all your network interfaces. If you have a large number of network interfaces, the operation fails unless you use pagination or one of the following filters: group-id , mac-address , private-dns-name , private-ip-address , subnet-id , or vpc-id . We strongly recommend using only paginated requests. Unpaginated requests are susceptible to throttling and timeouts.

## Input Shape: DescribeNetworkInterfacesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. association.allocation-id - The allocation ID returned when you allocated the Elastic IP address (I |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NetworkInterfaceIds | list[Any  # complex shape] |  | The network interface IDs. Default: Describes all your network interfaces. |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeNetworkInterfacesResult

- **NetworkInterfaces** (list[Any  # complex shape]): Information about the network interfaces.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_network_interfaces(store, request: dict) -> dict:
    """Describes the specified network interfaces or all your network interfaces. If you have a large number of network interfaces, the operation fails unless you use pagination or one of the following filte"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
