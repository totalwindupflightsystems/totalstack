---
id: "@specs/aws/lambda/list_durable_executions_by_function"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListDurableExecutionsByFunction"
---

# ListDurableExecutionsByFunction

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_durable_executions_by_function
> **spec:implements:** @kind:operation ListDurableExecutionsByFunction
> **AWS Protocol:** rest-json
> **HTTP:** GET /2025-12-01/functions/{FunctionName}/durable-executions
> **@ref:** specs/aws/lambda/docs/API_ListDurableExecutionsByFunction.spec.md

Returns a list of durable executions for a specified Lambda function. You can filter the results by execution name, status, and start time range. This API supports pagination for large result sets.

## Input Shape: ListDurableExecutionsByFunctionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DurableExecutionName | Any  # complex shape |  | Filter executions by name. Only executions with names that contain this string are returned. |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. You can specify a function name, a partial ARN, or a full ARN. |
| Marker | str |  | Pagination token from a previous request to continue retrieving results. |
| MaxItems | Any  # complex shape |  | Maximum number of executions to return (1-1000). Default is 100. |
| Qualifier | Any  # complex shape |  | The function version or alias. If not specified, lists executions for the $LATEST version. |
| ReverseOrder | Any  # complex shape |  | Set to true to return results in reverse chronological order (newest first). Default is false. |
| StartedAfter | Any  # complex shape |  | Filter executions that started after this timestamp (ISO 8601 format). |
| StartedBefore | Any  # complex shape |  | Filter executions that started before this timestamp (ISO 8601 format). |
| Statuses | list[Any  # complex shape] |  | Filter executions by status. Valid values: RUNNING, SUCCEEDED, FAILED, TIMED_OUT, STOPPED. |

## Output Shape: ListDurableExecutionsByFunctionResponse

- **DurableExecutions** (Any  # complex shape): List of durable execution summaries matching the filter criteria.
- **NextMarker** (str): Pagination token for retrieving additional results. Present only if there are more results available.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ServiceException**: The Lambda service encountered an internal error.
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def list_durable_executions_by_function(store, request: dict) -> dict:
    """Returns a list of durable executions for a specified Lambda function. You can filter the results by execution name, status, and start time range. This API supports pagination for large result sets."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    items = store.list_durable_executions_by_functions()
    return {"DurableExecutions": list(items.values())}
```
