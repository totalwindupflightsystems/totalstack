---
id: "@specs/aws/ec2/create_vpc_endpoint_connection_notification"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVpcEndpointConnectionNotification"
---

# CreateVpcEndpointConnectionNotification

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_vpc_endpoint_connection_notification
> **spec:implements:** @kind:operation CreateVpcEndpointConnectionNotification
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVpcEndpointConnectionNotification.spec.md

Creates a connection notification for a specified VPC endpoint or VPC endpoint service. A connection notification notifies you of specific endpoint events. You must create an SNS topic to receive notifications. For more information, see Creating an Amazon SNS topic in the Amazon SNS Developer Guide . You can create a connection notification for interface endpoints only.

## Input Shape: CreateVpcEndpointConnectionNotificationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| ConnectionEvents | list[str] | ✓ | The endpoint events for which to receive notifications. Valid values are Accept , Connect , Delete , and Reject . |
| ConnectionNotificationArn | str | ✓ | The ARN of the SNS topic for the notifications. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ServiceId | Any  # complex shape |  | The ID of the endpoint service. |
| VpcEndpointId | Any  # complex shape |  | The ID of the endpoint. |

## Output Shape: CreateVpcEndpointConnectionNotificationResult

- **ClientToken** (str): Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
- **ConnectionNotification** (Any  # complex shape): Information about the notification.

## Implementation

```speclang
def create_vpc_endpoint_connection_notification(store, request: dict) -> dict:
    """Creates a connection notification for a specified VPC endpoint or VPC endpoint service. A connection notification notifies you of specific endpoint events. You must create an SNS topic to receive noti"""
    connection_events = request.get("ConnectionEvents", "").strip() if isinstance(request.get("ConnectionEvents"), str) else request.get("ConnectionEvents")
    if not connection_events:
        raise ValidationException("ConnectionEvents is required")
    connection_notification_arn = request.get("ConnectionNotificationArn", "").strip() if isinstance(request.get("ConnectionNotificationArn"), str) else request.get("ConnectionNotificationArn")
    if not connection_notification_arn:
        raise ValidationException("ConnectionNotificationArn is required")

    if store.vpc_endpoint_connection_notifications(connection_notification_arn):
        raise ResourceInUseException(f"Resource connection_notification_arn already exists")

    record = {
        "DryRun": dry_run,
        "ServiceId": service_id,
        "VpcEndpointId": vpc_endpoint_id,
        "ConnectionNotificationArn": connection_notification_arn,
        "ConnectionEvents": connection_events,
        "ClientToken": client_token,
    }

    store.vpc_endpoint_connection_notifications(connection_notification_arn, record)

    return {
        "ConnectionNotification": record.get("ConnectionNotification", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
