---
id: "@specs/aws/lambda/send_durable_execution_callback_success"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_SendDurableExecutionCallbackSuccess"
---

# SendDurableExecutionCallbackSuccess

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/send_durable_execution_callback_success
> **spec:implements:** @kind:operation SendDurableExecutionCallbackSuccess
> **AWS Protocol:** rest-json
> **HTTP:** POST /2025-12-01/durable-execution-callbacks/{CallbackId}/succeed
> **@ref:** specs/aws/lambda/docs/API_SendDurableExecutionCallbackSuccess.spec.md

Sends a successful completion response for a callback operation in a durable execution. Use this API when an external system has successfully completed a callback operation.

## Input Shape: SendDurableExecutionCallbackSuccessRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallbackId | Any  # complex shape | ✓ | The unique identifier for the callback operation. |
| Result | Any  # complex shape |  | The result data from the successful callback operation. Maximum size is 256 KB. |

## Output Shape: SendDurableExecutionCallbackSuccessResponse


## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ServiceException**: The Lambda service encountered an internal error.
- **CallbackTimeoutException**: The callback ID token has either expired or the callback associated with the token has already been closed.

## Implementation

```speclang
def send_durable_execution_callback_success(store, request: dict) -> dict:
    """Sends a successful completion response for a callback operation in a durable execution. Use this API when an external system has successfully completed a callback operation."""
    callback_id = request.get("CallbackId", "").strip() if isinstance(request.get("CallbackId"), str) else request.get("CallbackId")
    if not callback_id:
        raise ValidationException("CallbackId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("SendDurableExecutionCallbackSuccess", request)
```
