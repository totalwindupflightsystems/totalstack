---
id: "@specs/aws/ec2/describe_vpc_endpoint_connection_notifications"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcEndpointConnectionNotifications"
---

# DescribeVpcEndpointConnectionNotifications

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_endpoint_connection_notifications
> **spec:implements:** @kind:operation DescribeVpcEndpointConnectionNotifications
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcEndpointConnectionNotifications.spec.md

Describes the connection notifications for VPC endpoints and VPC endpoint services.

## Input Shape: DescribeVpcEndpointConnectionNotificationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ConnectionNotificationId | Any  # complex shape |  | The ID of the notification. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. connection-notification-arn - The ARN of the SNS topic for the notification. connection-notification-id - T |
| MaxResults | int |  | The maximum number of results to return in a single call. To retrieve the remaining results, make another request with t |
| NextToken | str |  | The token to request the next page of results. |

## Output Shape: DescribeVpcEndpointConnectionNotificationsResult

- **ConnectionNotificationSet** (Any  # complex shape): The notifications.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_vpc_endpoint_connection_notifications(store, request: dict) -> dict:
    """Describes the connection notifications for VPC endpoints and VPC endpoint services."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
