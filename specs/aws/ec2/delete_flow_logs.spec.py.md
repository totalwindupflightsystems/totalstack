---
id: "@specs/aws/ec2/delete_flow_logs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteFlowLogs"
---

# DeleteFlowLogs

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_flow_logs
> **spec:implements:** @kind:operation DeleteFlowLogs
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteFlowLogs.spec.md

Deletes one or more flow logs.

## Input Shape: DeleteFlowLogsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FlowLogIds | list[Any  # complex shape] | ✓ | One or more flow log IDs. Constraint: Maximum of 1000 flow log IDs. |

## Output Shape: DeleteFlowLogsResult

- **Unsuccessful** (Any  # complex shape): Information about the flow logs that could not be deleted successfully.

## Implementation

```speclang
def delete_flow_logs(store, request: dict) -> dict:
    """Deletes one or more flow logs."""
    flow_log_ids = request.get("FlowLogIds", "").strip() if isinstance(request.get("FlowLogIds"), str) else request.get("FlowLogIds")

    if not store.flow_logss(flow_log_ids):
        raise ResourceNotFoundException(f"Resource flow_log_ids not found")
    store.delete_flow_logss(flow_log_ids)
    return {}
```
