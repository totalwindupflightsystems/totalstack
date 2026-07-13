---
id: "@specs/aws/ec2/describe_flow_logs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeFlowLogs"
---

# DescribeFlowLogs

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_flow_logs
> **spec:implements:** @kind:operation DescribeFlowLogs
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeFlowLogs.spec.md

Describes one or more flow logs. To view the published flow log records, you must view the log destination. For example, the CloudWatch Logs log group, the Amazon S3 bucket, or the Kinesis Data Firehose delivery stream.

## Input Shape: DescribeFlowLogsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filter | list[Any  # complex shape] |  | One or more filters. deliver-log-status - The status of the logs delivery ( SUCCESS | FAILED ). log-destination-type - T |
| FlowLogIds | list[Any  # complex shape] |  | One or more flow log IDs. Constraint: Maximum of 1000 flow log IDs. |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to request the next page of items. Pagination continues from the end of the items returned by the previous req |

## Output Shape: DescribeFlowLogsResult

- **FlowLogs** (Any  # complex shape): Information about the flow logs.
- **NextToken** (str): The token to request the next page of items. This value is null when there are no more items to return.

## Implementation

```speclang
def describe_flow_logs(store, request: dict) -> dict:
    """Describes one or more flow logs. To view the published flow log records, you must view the log destination. For example, the CloudWatch Logs log group, the Amazon S3 bucket, or the Kinesis Data Fireho"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
