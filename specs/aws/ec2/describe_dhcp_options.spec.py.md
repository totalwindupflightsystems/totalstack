---
id: "@specs/aws/ec2/describe_dhcp_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeDhcpOptions"
---

# DescribeDhcpOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_dhcp_options
> **spec:implements:** @kind:operation DescribeDhcpOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeDhcpOptions.spec.md

Describes your DHCP option sets. The default is to describe all your DHCP option sets. Alternatively, you can specify specific DHCP option set IDs or filter the results to include only the DHCP option sets that match specific criteria. For more information, see DHCP option sets in the Amazon VPC User Guide .

## Input Shape: DescribeDhcpOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DhcpOptionsIds | list[Any  # complex shape] |  | The IDs of DHCP option sets. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. dhcp-options-id - The ID of a DHCP options set. key - The key for one of the options (for example, domain-n |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeDhcpOptionsResult

- **DhcpOptions** (list[Any  # complex shape]): Information about the DHCP options sets.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_dhcp_options(store, request: dict) -> dict:
    """Describes your DHCP option sets. The default is to describe all your DHCP option sets. Alternatively, you can specify specific DHCP option set IDs or filter the results to include only the DHCP option"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
