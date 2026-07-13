---
id: "@specs/aws/ec2/describe_secondary_interfaces"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSecondaryInterfaces"
---

# DescribeSecondaryInterfaces

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_secondary_interfaces
> **spec:implements:** @kind:operation DescribeSecondaryInterfaces
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSecondaryInterfaces.spec.md

Describes one or more of your secondary interfaces.

## Input Shape: DescribeSecondaryInterfacesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. attachment.attachment-id - The ID of the secondary interface attachment. attachment.instance-id - The ID of |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| SecondaryInterfaceIds | list[Any  # complex shape] |  | The IDs of the secondary interfaces. |

## Output Shape: DescribeSecondaryInterfacesResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **SecondaryInterfaces** (list[Any  # complex shape]): Information about the secondary interfaces.

## Implementation

```speclang
def describe_secondary_interfaces(store, request: dict) -> dict:
    """Describes one or more of your secondary interfaces."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
