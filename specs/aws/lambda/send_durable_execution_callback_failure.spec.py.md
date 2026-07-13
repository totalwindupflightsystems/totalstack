---
id: "@specs/aws/lambda/send_durable_execution_callback_failure"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_SendDurableExecutionCallbackFailure"
---

# SendDurableExecutionCallbackFailure

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/send_durable_execution_callback_failure
> **spec:implements:** @kind:operation SendDurableExecutionCallbackFailure
> **AWS Protocol:** rest-json
> **HTTP:** POST /2025-12-01/durable-execution-callbacks/{CallbackId}/fail
> **@ref:** specs/aws/lambda/docs/API_SendDurableExecutionCallbackFailure.spec.md

Sends a failure response for a callback operation in a durable execution. Use this API when an external system cannot complete a callback operation successfully.

## Input Shape: SendDurableExecutionCallbackFailureRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallbackId | Any  # complex shape | ✓ | The unique identifier for the callback operation. |
| Error | Any  # complex shape |  | Error details describing why the callback operation failed. |

## Output Shape: SendDurableExecutionCallbackFailureResponse


## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ServiceException**: The Lambda service encountered an internal error.
- **CallbackTimeoutException**: The callback ID token has either expired or the callback associated with the token has already been closed.

## Implementation

```speclang
def send_durable_execution_callback_failure(store, request: dict) -> dict:
    """Sends a failure response for a callback operation in a durable execution. Use this API when an external system cannot complete a callback operation successfully."""
    callback_id = request.get("CallbackId", "").strip() if isinstance(request.get("CallbackId"), str) else request.get("CallbackId")
    if not callback_id:
        raise ValidationException("CallbackId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("SendDurableExecutionCallbackFailure", request)
```
