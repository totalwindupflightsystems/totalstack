---
id: "@specs/aws/ec2/create_flow_logs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateFlowLogs"
---

# CreateFlowLogs

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_flow_logs
> **spec:implements:** @kind:operation CreateFlowLogs
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateFlowLogs.spec.md

Creates one or more flow logs to capture information about IP traffic for a specific network interface, subnet, or VPC. Flow log data for a monitored network interface is recorded as flow log records, which are log events consisting of fields that describe the traffic flow. For more information, see Flow log records in the Amazon VPC User Guide . When publishing to CloudWatch Logs, flow log records are published to a log group, and each network interface has a unique log stream in the log group. When publishing to Amazon S3, flow log records for all of the monitored network interfaces are published to a single log file object that is stored in the specified bucket. For more information, see VPC Flow Logs in the Amazon VPC User Guide .

## Input Shape: CreateFlowLogsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| DeliverCrossAccountRole | str |  | The ARN of the IAM role that allows Amazon EC2 to publish flow logs across accounts. |
| DeliverLogsPermissionArn | str |  | The ARN of the IAM role that allows Amazon EC2 to publish flow logs to the log destination. This parameter is required i |
| DestinationOptions | Any  # complex shape |  | The destination options. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LogDestination | str |  | The destination for the flow log data. The meaning of this parameter depends on the destination type. If the destination |
| LogDestinationType | Any  # complex shape |  | The type of destination for the flow log data. Default: cloud-watch-logs |
| LogFormat | str |  | The fields to include in the flow log record. List the fields in the order in which they should appear. If you omit this |
| LogGroupName | str |  | The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs. This parameter is val |
| MaxAggregationInterval | int |  | The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. The possi |
| ResourceIds | Any  # complex shape | ✓ | The IDs of the resources to monitor. For example, if the resource type is VPC , specify the IDs of the VPCs. Constraints |
| ResourceType | Any  # complex shape | ✓ | The type of resource to monitor. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the flow logs. |
| TrafficType | Any  # complex shape |  | The type of traffic to monitor (accepted traffic, rejected traffic, or all traffic). This parameter is not supported for |

## Output Shape: CreateFlowLogsResult

- **ClientToken** (str): Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
- **FlowLogIds** (list[str]): The IDs of the flow logs.
- **Unsuccessful** (Any  # complex shape): Information about the flow logs that could not be created successfully.

## Implementation

```speclang
def create_flow_logs(store, request: dict) -> dict:
    """Creates one or more flow logs to capture information about IP traffic for a specific network interface, subnet, or VPC. Flow log data for a monitored network interface is recorded as flow log records,"""
    resource_ids = request.get("ResourceIds", "").strip() if isinstance(request.get("ResourceIds"), str) else request.get("ResourceIds")
    if not resource_ids:
        raise ValidationException("ResourceIds is required")
    resource_type = request.get("ResourceType", "").strip() if isinstance(request.get("ResourceType"), str) else request.get("ResourceType")
    if not resource_type:
        raise ValidationException("ResourceType is required")

    if store.flow_logss(resource_ids):
        raise ResourceInUseException(f"Resource resource_ids already exists")

    record = {
        "DryRun": dry_run,
        "ClientToken": client_token,
        "DeliverLogsPermissionArn": deliver_logs_permission_arn,
        "DeliverCrossAccountRole": deliver_cross_account_role,
        "LogGroupName": log_group_name,
        "ResourceIds": resource_ids,
        "ResourceType": resource_type,
        "TrafficType": traffic_type,
        "LogDestinationType": log_destination_type,
        "LogDestination": log_destination,
        "LogFormat": log_format,
        "TagSpecifications": tag_specifications,
        "MaxAggregationInterval": max_aggregation_interval,
        "DestinationOptions": destination_options,
    }

    store.flow_logss(resource_ids, record)

    return {
        "ClientToken": record.get("ClientToken", {}),
        "FlowLogIds": record.get("FlowLogIds", {}),
        "Unsuccessful": record.get("Unsuccessful", {}),
    }
```
