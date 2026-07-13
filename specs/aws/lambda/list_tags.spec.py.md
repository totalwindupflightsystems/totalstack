---
id: "@specs/aws/lambda/list_tags"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListTags"
---

# ListTags

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_tags
> **spec:implements:** @kind:operation ListTags
> **AWS Protocol:** rest-json
> **HTTP:** GET /2017-03-31/tags/{Resource}
> **@ref:** specs/aws/lambda/docs/API_ListTags.spec.md

Returns a function, event source mapping, or code signing configuration's tags . You can also view function tags with GetFunction .

## Input Shape: ListTagsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Resource | Any  # complex shape | ✓ | The resource's Amazon Resource Name (ARN). Note: Lambda does not support adding tags to function aliases or versions. |

## Output Shape: ListTagsResponse

- **Tags** (Any  # complex shape): The function's tags.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def list_tags(store, request: dict) -> dict:
    """Returns a function, event source mapping, or code signing configuration's tags . You can also view function tags with GetFunction ."""
    resource = request.get("Resource", "").strip() if isinstance(request.get("Resource"), str) else request.get("Resource")
    if not resource:
        raise ValidationException("Resource is required")

    items = store.list_tagss()
    return {"Tags": list(items.values())}
```
