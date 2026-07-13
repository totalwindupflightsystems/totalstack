---
id: "@specs/aws/lambda/tag_resource"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_TagResource"
---

# TagResource

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/tag_resource
> **spec:implements:** @kind:operation TagResource
> **AWS Protocol:** rest-json
> **HTTP:** POST /2017-03-31/tags/{Resource}
> **@ref:** specs/aws/lambda/docs/API_TagResource.spec.md

Adds tags to a function, event source mapping, or code signing configuration.

## Input Shape: TagResourceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Resource | Any  # complex shape | ✓ | The resource's Amazon Resource Name (ARN). |
| Tags | Any  # complex shape | ✓ | A list of tags to apply to the resource. |

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def tag_resource(store, request: dict) -> dict:
    """Adds tags to a function, event source mapping, or code signing configuration."""
    resource = request.get("Resource", "").strip() if isinstance(request.get("Resource"), str) else request.get("Resource")
    if not resource:
        raise ValidationException("Resource is required")
    tags = request.get("Tags", "").strip() if isinstance(request.get("Tags"), str) else request.get("Tags")
    if not tags:
        raise ValidationException("Tags is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
