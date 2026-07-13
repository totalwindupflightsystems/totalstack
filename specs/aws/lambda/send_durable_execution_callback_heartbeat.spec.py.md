---
id: "@specs/aws/lambda/send_durable_execution_callback_heartbeat"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_SendDurableExecutionCallbackHeartbeat"
---

# SendDurableExecutionCallbackHeartbeat

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/send_durable_execution_callback_heartbeat
> **spec:implements:** @kind:operation SendDurableExecutionCallbackHeartbeat
> **AWS Protocol:** rest-json
> **HTTP:** POST /2025-12-01/durable-execution-callbacks/{CallbackId}/heartbeat
> **@ref:** specs/aws/lambda/docs/API_SendDurableExecutionCallbackHeartbeat.spec.md

Sends a heartbeat signal for a long-running callback operation to prevent timeout. Use this API to extend the callback timeout period while the external operation is still in progress.

## Input Shape: SendDurableExecutionCallbackHeartbeatRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallbackId | Any  # complex shape | ✓ | The unique identifier for the callback operation. |

## Output Shape: SendDurableExecutionCallbackHeartbeatResponse


## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ServiceException**: The Lambda service encountered an internal error.
- **CallbackTimeoutException**: The callback ID token has either expired or the callback associated with the token has already been closed.

## Implementation

```speclang
def send_durable_execution_callback_heartbeat(store, request: dict) -> dict:
    """Sends a heartbeat signal for a long-running callback operation to prevent timeout. Use this API to extend the callback timeout period while the external operation is still in progress."""
    callback_id = request.get("CallbackId", "").strip() if isinstance(request.get("CallbackId"), str) else request.get("CallbackId")
    if not callback_id:
        raise ValidationException("CallbackId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("SendDurableExecutionCallbackHeartbeat", request)
```
