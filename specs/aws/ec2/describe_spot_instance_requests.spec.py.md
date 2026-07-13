---
id: "@specs/aws/ec2/describe_spot_instance_requests"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSpotInstanceRequests"
---

# DescribeSpotInstanceRequests

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_spot_instance_requests
> **spec:implements:** @kind:operation DescribeSpotInstanceRequests
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSpotInstanceRequests.spec.md

Describes the specified Spot Instance requests. You can use DescribeSpotInstanceRequests to find a running Spot Instance by examining the response. If the status of the Spot Instance is fulfilled , the instance ID appears in the response and contains the identifier of the instance. Alternatively, you can use DescribeInstances with a filter to look for instances where the instance lifecycle is spot . We recommend that you set MaxResults to a value between 5 and 1000 to limit the number of items returned. This paginates the output, which makes the list more manageable and returns the items faster. If the list of items exceeds your MaxResults value, then that number of items is returned along with a NextToken value that can be passed to a subsequent DescribeSpotInstanceRequests request to retrieve the remaining items. Spot Instance requests are deleted four hours after they are canceled and their instances are terminated.

## Input Shape: DescribeSpotInstanceRequestsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. availability-zone-group - The Availability Zone group. create-time - The time stamp when the Spot Instance  |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| SpotInstanceRequestIds | list[Any  # complex shape] |  | The IDs of the Spot Instance requests. |

## Output Shape: DescribeSpotInstanceRequestsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **SpotInstanceRequests** (list[Any  # complex shape]): The Spot Instance requests.

## Implementation

```speclang
def describe_spot_instance_requests(store, request: dict) -> dict:
    """Describes the specified Spot Instance requests. You can use DescribeSpotInstanceRequests to find a running Spot Instance by examining the response. If the status of the Spot Instance is fulfilled , th"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
