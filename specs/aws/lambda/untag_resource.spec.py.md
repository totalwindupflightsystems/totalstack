---
id: "@specs/aws/lambda/untag_resource"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_UntagResource"
---

# UntagResource

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/untag_resource
> **spec:implements:** @kind:operation UntagResource
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2017-03-31/tags/{Resource}
> **@ref:** specs/aws/lambda/docs/API_UntagResource.spec.md

Removes tags from a function, event source mapping, or code signing configuration.

## Input Shape: UntagResourceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Resource | Any  # complex shape | ✓ | The resource's Amazon Resource Name (ARN). |
| TagKeys | list[Any  # complex shape] | ✓ | A list of tag keys to remove from the resource. |

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def untag_resource(store, request: dict) -> dict:
    """Removes tags from a function, event source mapping, or code signing configuration."""
    resource = request.get("Resource", "").strip() if isinstance(request.get("Resource"), str) else request.get("Resource")
    if not resource:
        raise ValidationException("Resource is required")
    tag_keys = request.get("TagKeys", "").strip() if isinstance(request.get("TagKeys"), str) else request.get("TagKeys")
    if not tag_keys:
        raise ValidationException("TagKeys is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
