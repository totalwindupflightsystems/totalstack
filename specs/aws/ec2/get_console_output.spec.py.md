---
id: "@specs/aws/ec2/get_console_output"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetConsoleOutput"
---

# GetConsoleOutput

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_console_output
> **spec:implements:** @kind:operation GetConsoleOutput
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetConsoleOutput.spec.md

Gets the console output for the specified instance. For Linux instances, the instance console output displays the exact console output that would normally be displayed on a physical monitor attached to a computer. For Windows instances, the instance console output includes the last three system event log errors. For more information, see Instance console output in the Amazon EC2 User Guide .

## Input Shape: GetConsoleOutputRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |
| Latest | bool |  | When enabled, retrieves the latest console output for the instance. Default: disabled ( false ) |

## Output Shape: GetConsoleOutputResult

- **InstanceId** (str): The ID of the instance.
- **Output** (str): The console output, base64-encoded. If you are using a command line tool, the tool decodes the output for you.
- **Timestamp** (Any  # complex shape): The time at which the output was last updated.

## Implementation

```speclang
def get_console_output(store, request: dict) -> dict:
    """Gets the console output for the specified instance. For Linux instances, the instance console output displays the exact console output that would normally be displayed on a physical monitor attached t"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    if store.console_outputs(instance_id):
        raise ResourceInUseException(f"Resource instance_id already exists")

    record = {
        "InstanceId": instance_id,
        "Latest": latest,
        "DryRun": dry_run,
    }

    store.console_outputs(instance_id, record)

    return {
        "InstanceId": instance_id,
        "Timestamp": record.get("Timestamp", {}),
        "Output": record.get("Output", {}),
    }
```
