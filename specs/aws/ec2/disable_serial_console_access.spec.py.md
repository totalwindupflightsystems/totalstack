---
id: "@specs/aws/ec2/disable_serial_console_access"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableSerialConsoleAccess"
---

# DisableSerialConsoleAccess

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_serial_console_access
> **spec:implements:** @kind:operation DisableSerialConsoleAccess
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableSerialConsoleAccess.spec.md

Disables access to the EC2 serial console of all instances for your account. By default, access to the EC2 serial console is disabled for your account. For more information, see Manage account access to the EC2 serial console in the Amazon EC2 User Guide .

## Input Shape: DisableSerialConsoleAccessRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DisableSerialConsoleAccessResult

- **SerialConsoleAccessEnabled** (bool): If true , access to the EC2 serial console of all instances is enabled for your account. If false , access to the EC2 se

## Implementation

```speclang
def disable_serial_console_access(store, request: dict) -> dict:
    """Disables access to the EC2 serial console of all instances for your account. By default, access to the EC2 serial console is disabled for your account. For more information, see Manage account access """

```
