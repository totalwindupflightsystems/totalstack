---
id: "@specs/aws/ec2/send_diagnostic_interrupt"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_SendDiagnosticInterrupt"
---

# SendDiagnosticInterrupt

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/send_diagnostic_interrupt
> **spec:implements:** @kind:operation SendDiagnosticInterrupt
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_SendDiagnosticInterrupt.spec.md

Sends a diagnostic interrupt to the specified Amazon EC2 instance to trigger a kernel panic (on Linux instances), or a blue screen / stop error (on Windows instances). For instances based on Intel and AMD processors, the interrupt is received as a non-maskable interrupt (NMI). In general, the operating system crashes and reboots when a kernel panic or stop error is triggered. The operating system can also be configured to perform diagnostic tasks, such as generating a memory dump file, loading a secondary kernel, or obtaining a call trace. Before sending a diagnostic interrupt to your instance, ensure that its operating system is configured to perform the required diagnostic tasks. For more information about configuring your operating system to generate a crash dump when a kernel panic or stop error occurs, see Send a diagnostic interrupt (for advanced users) in the Amazon EC2 User Guide .

## Input Shape: SendDiagnosticInterruptRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |

## Implementation

```speclang
def send_diagnostic_interrupt(store, request: dict) -> dict:
    """Sends a diagnostic interrupt to the specified Amazon EC2 instance to trigger a kernel panic (on Linux instances), or a blue screen / stop error (on Windows instances). For instances based on Intel and"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("SendDiagnosticInterrupt", request)
```
