---
id: "@specs/aws/lambda/list_functions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListFunctions"
---

# ListFunctions

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_functions
> **spec:implements:** @kind:operation ListFunctions
> **AWS Protocol:** rest-json
> **HTTP:** GET /2015-03-31/functions
> **@ref:** specs/aws/lambda/docs/API_ListFunctions.spec.md

Returns a list of Lambda functions, with the version-specific configuration of each. Lambda returns up to 50 functions per call. Set FunctionVersion to ALL to include all published versions of each function in addition to the unpublished version. The ListFunctions operation returns a subset of the FunctionConfiguration fields. To get the additional fields (State, StateReasonCode, StateReason, LastUpdateStatus, LastUpdateStatusReason, LastUpdateStatusReasonCode, RuntimeVersionConfig) for a function or version, use GetFunction .

## Input Shape: ListFunctionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionVersion | Any  # complex shape |  | Set to ALL to include entries for all published versions of each function. |
| Marker | str |  | Specify the pagination token that's returned by a previous request to retrieve the next page of results. |
| MasterRegion | Any  # complex shape |  | For Lambda@Edge functions, the Amazon Web Services Region of the master function. For example, us-east-1 filters the lis |
| MaxItems | Any  # complex shape |  | The maximum number of functions to return in the response. Note that ListFunctions returns a maximum of 50 items in each |

## Output Shape: ListFunctionsResponse

- **Functions** (list[Any  # complex shape]): A list of Lambda functions.
- **NextMarker** (str): The pagination token that's included if more results are available.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .

## Implementation

```speclang
def list_functions(store, request: dict) -> dict:
    """Returns a list of Lambda functions, with the version-specific configuration of each. Lambda returns up to 50 functions per call. Set FunctionVersion to ALL to include all published versions of each fu"""

    items = store.list_functionss()
    return {"Functions": list(items.values())}
```
