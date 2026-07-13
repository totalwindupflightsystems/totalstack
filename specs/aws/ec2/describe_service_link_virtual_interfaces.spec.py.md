---
id: "@specs/aws/ec2/describe_service_link_virtual_interfaces"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeServiceLinkVirtualInterfaces"
---

# DescribeServiceLinkVirtualInterfaces

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_service_link_virtual_interfaces
> **spec:implements:** @kind:operation DescribeServiceLinkVirtualInterfaces
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeServiceLinkVirtualInterfaces.spec.md

Describes the Outpost service link virtual interfaces.

## Input Shape: DescribeServiceLinkVirtualInterfacesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters to use for narrowing down the request. The following filters are supported: outpost-lag-id - The ID of the O |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| ServiceLinkVirtualInterfaceIds | Any  # complex shape |  | The IDs of the service link virtual interfaces. |

## Output Shape: DescribeServiceLinkVirtualInterfacesResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **ServiceLinkVirtualInterfaces** (Any  # complex shape): Describes the service link virtual interfaces.

## Implementation

```speclang
def describe_service_link_virtual_interfaces(store, request: dict) -> dict:
    """Describes the Outpost service link virtual interfaces."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
