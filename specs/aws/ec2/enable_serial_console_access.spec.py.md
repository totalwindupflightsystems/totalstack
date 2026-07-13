---
id: "@specs/aws/ec2/enable_serial_console_access"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableSerialConsoleAccess"
---

# EnableSerialConsoleAccess

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_serial_console_access
> **spec:implements:** @kind:operation EnableSerialConsoleAccess
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableSerialConsoleAccess.spec.md

Enables access to the EC2 serial console of all instances for your account. By default, access to the EC2 serial console is disabled for your account. For more information, see Manage account access to the EC2 serial console in the Amazon EC2 User Guide .

## Input Shape: EnableSerialConsoleAccessRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: EnableSerialConsoleAccessResult

- **SerialConsoleAccessEnabled** (bool): If true , access to the EC2 serial console of all instances is enabled for your account. If false , access to the EC2 se

## Implementation

```speclang
def enable_serial_console_access(store, request: dict) -> dict:
    """Enables access to the EC2 serial console of all instances for your account. By default, access to the EC2 serial console is disabled for your account. For more information, see Manage account access t"""

```
