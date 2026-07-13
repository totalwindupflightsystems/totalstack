---
id: "@specs/aws/ec2/describe_instance_event_windows"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeInstanceEventWindows"
---

# DescribeInstanceEventWindows

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_instance_event_windows
> **spec:implements:** @kind:operation DescribeInstanceEventWindows
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeInstanceEventWindows.spec.md

Describes the specified event windows or all event windows. If you specify event window IDs, the output includes information for only the specified event windows. If you specify filters, the output includes information for only those event windows that meet the filter criteria. If you do not specify event windows IDs or filters, the output includes information for all event windows, which can affect performance. We recommend that you use pagination to ensure that the operation returns quickly and successfully. For more information, see Define event windows for scheduled events in the Amazon EC2 User Guide .

## Input Shape: DescribeInstanceEventWindowsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. dedicated-host-id - The event windows associated with the specified Dedicated Host ID. event-window |
| InstanceEventWindowIds | Any  # complex shape |  | The IDs of the event windows. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the  |
| NextToken | str |  | The token to request the next page of results. |

## Output Shape: DescribeInstanceEventWindowsResult

- **InstanceEventWindows** (Any  # complex shape): Information about the event windows.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_instance_event_windows(store, request: dict) -> dict:
    """Describes the specified event windows or all event windows. If you specify event window IDs, the output includes information for only the specified event windows. If you specify filters, the output in"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
