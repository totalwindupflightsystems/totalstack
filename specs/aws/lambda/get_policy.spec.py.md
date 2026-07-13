---
id: "@specs/aws/lambda/get_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetPolicy"
---

# GetPolicy

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_policy
> **spec:implements:** @kind:operation GetPolicy
> **AWS Protocol:** rest-json
> **HTTP:** GET /2015-03-31/functions/{FunctionName}/policy
> **@ref:** specs/aws/lambda/docs/API_GetPolicy.spec.md

Returns the resource-based IAM policy for a function, version, or alias.

## Input Shape: GetPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function, version, or alias. Name formats Function name – my-function (name-only), my-func |
| Qualifier | Any  # complex shape |  | Specify a version or alias to get the policy for that resource. |

## Output Shape: GetPolicyResponse

- **Policy** (str): The resource-based policy.
- **RevisionId** (str): A unique identifier for the current revision of the policy.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_policy(store, request: dict) -> dict:
    """Returns the resource-based IAM policy for a function, version, or alias."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    resource = store.policys(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")
    return {"FunctionName": function_name, **resource}
```
