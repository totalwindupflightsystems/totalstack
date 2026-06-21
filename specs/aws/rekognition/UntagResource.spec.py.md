---
id: "@specs/aws/rekognition/untag_resource"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# UntagResource

Removes one or more tags from an Amazon Rekognition collection, stream processor, or Custom Labels model. This operation requires permissions to perform the rekognition:UntagResource action.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ResourceArn` | ResourceArn | Yes | Amazon Resource Name (ARN) of the model, collection, or stream processor that you want to remove the |
| `TagKeys` | TagKeyList | Yes | A list of the tags that you want to remove. |

## Errors
- `AccessDeniedException`
- `InternalServerError`
- `InvalidParameterException`
- `ProvisionedThroughputExceededException`
- `ResourceNotFoundException`
- `ThrottlingException`

## Output Members
- (none)

## Implementation

```speclang
@dataclass
@kind: operation
def execute_untag_resource(store, request):
    """Removes one or more tags from an Amazon Rekognition collection, stream processor, or Custom Labels model. This operation requires permissions to perform the rekognition:UntagResource action."""
    if not request.get("ResourceArn"):
        raise InvalidParameterException(f"{fname} is required")
    if not request.get("TagKeys"):
        raise InvalidParameterException(f"{fname} is required")
    resource_arn = request["ResourceArn"]
    tag_keys = request["TagKeys"]
    if resource_arn in store.tags:
        for key in tag_keys:
            store.tags[resource_arn].pop(key, None)
    return {}
```
