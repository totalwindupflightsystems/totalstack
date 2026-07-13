---
id: "@specs/aws/ec2/describe_instance_image_metadata"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeInstanceImageMetadata"
---

# DescribeInstanceImageMetadata

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_instance_image_metadata
> **spec:implements:** @kind:operation DescribeInstanceImageMetadata
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeInstanceImageMetadata.spec.md

Describes the AMI that was used to launch an instance, even if the AMI is deprecated, deregistered, made private (no longer public or shared with your account), or not allowed. If you specify instance IDs, the output includes information for only the specified instances. If you specify filters, the output includes information for only those instances that meet the filter criteria. If you do not specify instance IDs or filters, the output includes information for all instances, which can affect performance. If you specify an instance ID that is not valid, an instance that doesn't exist, or an instance that you do not own, an error ( InvalidInstanceID.NotFound ) is returned. Recently terminated instances might appear in the returned results. This interval is usually less than one hour. In the rare case where an Availability Zone is experiencing a service disruption and you specify instance IDs that are in the affected Availability Zone, or do not specify any instance IDs at all, the call fails. If you specify only instance IDs that are in an unaffected Availability Zone, the call works normally. The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeInstanceImageMetadataRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. availability-zone - The name of the Availability Zone (for example, us-west-2a ) or Local Zone (for example |
| InstanceIds | list[Any  # complex shape] |  | The instance IDs. If you don't specify an instance ID or filters, the output includes information for all instances. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeInstanceImageMetadataResult

- **InstanceImageMetadata** (list[Any  # complex shape]): Information about the instance and the AMI used to launch the instance.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_instance_image_metadata(store, request: dict) -> dict:
    """Describes the AMI that was used to launch an instance, even if the AMI is deprecated, deregistered, made private (no longer public or shared with your account), or not allowed. If you specify instance"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
