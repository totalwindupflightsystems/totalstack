---
id: "@specs/aws/ec2/modify_vpc_endpoint_connection_notification"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpcEndpointConnectionNotification"
---

# ModifyVpcEndpointConnectionNotification

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpc_endpoint_connection_notification
> **spec:implements:** @kind:operation ModifyVpcEndpointConnectionNotification
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpcEndpointConnectionNotification.spec.md

Modifies a connection notification for VPC endpoint or VPC endpoint service. You can change the SNS topic for the notification, or the events for which to be notified.

## Input Shape: ModifyVpcEndpointConnectionNotificationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ConnectionEvents | list[str] |  | The events for the endpoint. Valid values are Accept , Connect , Delete , and Reject . |
| ConnectionNotificationArn | str |  | The ARN for the SNS topic for the notification. |
| ConnectionNotificationId | Any  # complex shape | ✓ | The ID of the notification. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: ModifyVpcEndpointConnectionNotificationResult

- **ReturnValue** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def modify_vpc_endpoint_connection_notification(store, request: dict) -> dict:
    """Modifies a connection notification for VPC endpoint or VPC endpoint service. You can change the SNS topic for the notification, or the events for which to be notified."""
    connection_notification_id = request.get("ConnectionNotificationId", "").strip() if isinstance(request.get("ConnectionNotificationId"), str) else request.get("ConnectionNotificationId")
    if not connection_notification_id:
        raise ValidationException("ConnectionNotificationId is required")

    resource = store.vpc_endpoint_connection_notifications(connection_notification_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource connection_notification_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "ConnectionNotificationArn" in request:
        resource["ConnectionNotificationArn"] = connection_notification_arn
    if "ConnectionEvents" in request:
        resource["ConnectionEvents"] = connection_events

    store.vpc_endpoint_connection_notifications(connection_notification_id, resource)
    return resource
```
