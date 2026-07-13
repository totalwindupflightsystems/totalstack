---
id: "@specs/aws/ec2/delete_vpc_endpoint_connection_notifications"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVpcEndpointConnectionNotifications"
---

# DeleteVpcEndpointConnectionNotifications

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_vpc_endpoint_connection_notifications
> **spec:implements:** @kind:operation DeleteVpcEndpointConnectionNotifications
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVpcEndpointConnectionNotifications.spec.md

Deletes the specified VPC endpoint connection notifications.

## Input Shape: DeleteVpcEndpointConnectionNotificationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ConnectionNotificationIds | list[Any  # complex shape] | ✓ | The IDs of the notifications. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DeleteVpcEndpointConnectionNotificationsResult

- **Unsuccessful** (Any  # complex shape): Information about the notifications that could not be deleted successfully.

## Implementation

```speclang
def delete_vpc_endpoint_connection_notifications(store, request: dict) -> dict:
    """Deletes the specified VPC endpoint connection notifications."""
    connection_notification_ids = request.get("ConnectionNotificationIds", "").strip() if isinstance(request.get("ConnectionNotificationIds"), str) else request.get("ConnectionNotificationIds")

    if not store.vpc_endpoint_connection_notificationss(connection_notification_ids):
        raise ResourceNotFoundException(f"Resource connection_notification_ids not found")
    store.delete_vpc_endpoint_connection_notificationss(connection_notification_ids)
    return {}
```
