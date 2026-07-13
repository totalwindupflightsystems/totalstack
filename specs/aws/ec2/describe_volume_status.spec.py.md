---
id: "@specs/aws/ec2/describe_volume_status"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVolumeStatus"
---

# DescribeVolumeStatus

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_volume_status
> **spec:implements:** @kind:operation DescribeVolumeStatus
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVolumeStatus.spec.md

Describes the status of the specified volumes. Volume status provides the result of the checks performed on your volumes to determine events that can impair the performance of your volumes. The performance of a volume can be affected if an issue occurs on the volume's underlying host. If the volume's underlying host experiences a power outage or system issue, after the system is restored, there could be data inconsistencies on the volume. Volume events notify you if this occurs. Volume actions notify you if any action needs to be taken in response to the event. The DescribeVolumeStatus operation provides the following information about the specified volumes: Status : Reflects the current status of the volume. The possible values are ok , impaired , warning , or insufficient-data . If all checks pass, the overall status of the volume is ok . If the check fails, the overall status is impaired . If the status is insufficient-data , then the checks might still be taking place on your volume at the time. We recommend that you retry the request. For more information about volume status, see Monitor the status of your volumes in the Amazon EBS User Guide . Events : Reflect the cause of a volume status and might require you to take action. For example, if your volume returns an impaired status, then the volume event might be potential-data-inconsistency . This means that your volume has been affected by an issue with the underlying host, has all I/O operations disabled, and might have inconsistent data. Actions : Reflect the actions you might have to take in response to an event. For example, if the status of the volume is impaired and the volume event shows potential-data-inconsistency , then the action shows enable-volume-io . This means that you may want to enable the I/O operations for the volume and then check the volume for data consistency. For more information, see Work with an impaired EBS volume . Volume status is based on the volume status checks, and does not reflect the volume state. Therefore, volume status does not indicate volumes in the error state (for example, when a volume is incapable of accepting I/O.) The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeVolumeStatusRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. action.code - The action code for the event (for example, enable-volume-io ). action.description - A descri |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| VolumeIds | list[Any  # complex shape] |  | The IDs of the volumes. Default: Describes all your volumes. |

## Output Shape: DescribeVolumeStatusResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **VolumeStatuses** (list[Any  # complex shape]): Information about the status of the volumes.

## Implementation

```speclang
def describe_volume_status(store, request: dict) -> dict:
    """Describes the status of the specified volumes. Volume status provides the result of the checks performed on your volumes to determine events that can impair the performance of your volumes. The perfor"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
