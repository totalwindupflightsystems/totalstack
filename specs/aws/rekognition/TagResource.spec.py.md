---
id: "@specs/aws/rekognition/tag_resource"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# TagResource

Adds one or more key-value tags to an Amazon Rekognition collection, stream processor, or Custom Labels model. For more information, see Tagging AWS Resources. This operation requires permissions to perform the rekognition:TagResource action.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ResourceArn` | ResourceArn | Yes | Amazon Resource Name (ARN) of the model, collection, or stream processor that you want to assign the |
| `Tags` | TagMap | Yes | The key-value tags to assign to the resource. |

## Errors
- `AccessDeniedException`
- `InternalServerError`
- `InvalidParameterException`
- `ProvisionedThroughputExceededException`
- `ResourceNotFoundException`
- `ServiceQuotaExceededException`
- `ThrottlingException`

## Output Members
- (none)

## Implementation

```speclang
@dataclass
@kind: operation
def execute_tag_resource(store, request):
    """Adds one or more key-value tags to an Amazon Rekognition collection, stream processor, or Custom Labels model. For more information, see Tagging AWS Resources. This operation requires permissions to perform the rekognition:TagResource action."""
    if not request.get("ResourceArn"):
        raise InvalidParameterException(f"{fname} is required")
    if not request.get("Tags"):
        raise InvalidParameterException(f"{fname} is required")
    resource_arn = request["ResourceArn"]
    tags = request["Tags"]
    if resource_arn not in store.tags:
        store.tags[resource_arn] = {}
    store.tags[resource_arn].update(tags)
    return {}
```
