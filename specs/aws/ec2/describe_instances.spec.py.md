---
id: "@specs/aws/ec2/describe_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeInstances"
---

# DescribeInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_instances
> **spec:implements:** @kind:operation DescribeInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeInstances.spec.md

Describes the specified instances or all instances. If you specify instance IDs, the output includes information for only the specified instances. If you specify filters, the output includes information for only those instances that meet the filter criteria. If you do not specify instance IDs or filters, the output includes information for all instances, which can affect performance. We recommend that you use pagination to ensure that the operation returns quickly and successfully. The response includes SQL license exemption status information for instances registered with the SQL LE service, providing visibility into license exemption configuration and status. If you specify an instance ID that is not valid, an error is returned. If you specify an instance that you do not own, it is not included in the output. Recently terminated instances might appear in the returned results. This interval is usually less than one hour. If you describe instances in the rare case where an Availability Zone is experiencing a service disruption and you specify instance IDs that are in the affected zone, or do not specify any instance IDs at all, the call fails. If you describe instances and specify only instance IDs that are in an unaffected zone, the call works normally. The Amazon EC2 API follows an eventual consistency model. This means that the result of an API command you run that creates or modifies resources might not be immediately available to all subsequent commands you run. For guidance on how to manage eventual consistency, see Eventual consistency in the Amazon EC2 API in the Amazon EC2 Developer Guide . We strongly recommend using only paginated requests. Unpaginated requests are susceptible to throttling and timeouts. The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| Filters | list[Any  # complex shape] |  | The filters. affinity - The affinity setting for an instance running on a Dedicated Host ( default | host ). architectur |
| InstanceIds | list[Any  # complex shape] |  | The instance IDs. Default: Describes all your instances. |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeInstancesResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **Reservations** (list[Any  # complex shape]): Information about the reservations.

## Implementation

```speclang
def describe_instances(store, request: dict) -> dict:
    """Describes the specified instances or all instances. If you specify instance IDs, the output includes information for only the specified instances. If you specify filters, the output includes informati"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
