---
id: "@specs/aws/ec2/get_aws_network_performance_data"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetAwsNetworkPerformanceData"
---

# GetAwsNetworkPerformanceData

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_aws_network_performance_data
> **spec:implements:** @kind:operation GetAwsNetworkPerformanceData
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetAwsNetworkPerformanceData.spec.md

Gets network performance data.

## Input Shape: GetAwsNetworkPerformanceDataRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DataQueries | Any  # complex shape |  | A list of network performance data queries. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EndTime | Any  # complex shape |  | The ending time for the performance data request. The end time must be formatted as yyyy-mm-ddThh:mm:ss . For example, 2 |
| MaxResults | int |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| StartTime | Any  # complex shape |  | The starting time for the performance data request. The starting time must be formatted as yyyy-mm-ddThh:mm:ss . For exa |

## Output Shape: GetAwsNetworkPerformanceDataResult

- **DataResponses** (Any  # complex shape): The list of data responses.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_aws_network_performance_data(store, request: dict) -> dict:
    """Gets network performance data."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
