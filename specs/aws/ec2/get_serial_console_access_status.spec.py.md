---
id: "@specs/aws/ec2/get_serial_console_access_status"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetSerialConsoleAccessStatus"
---

# GetSerialConsoleAccessStatus

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_serial_console_access_status
> **spec:implements:** @kind:operation GetSerialConsoleAccessStatus
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetSerialConsoleAccessStatus.spec.md

Retrieves the access status of your account to the EC2 serial console of all instances. By default, access to the EC2 serial console is disabled for your account. For more information, see Manage account access to the EC2 serial console in the Amazon EC2 User Guide .

## Input Shape: GetSerialConsoleAccessStatusRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: GetSerialConsoleAccessStatusResult

- **ManagedBy** (Any  # complex shape): The entity that manages access to the serial console. Possible values include: account - Access is managed by the accoun
- **SerialConsoleAccessEnabled** (bool): If true , access to the EC2 serial console of all instances is enabled for your account. If false , access to the EC2 se

## Implementation

```speclang
def get_serial_console_access_status(store, request: dict) -> dict:
    """Retrieves the access status of your account to the EC2 serial console of all instances. By default, access to the EC2 serial console is disabled for your account. For more information, see Manage acco"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
