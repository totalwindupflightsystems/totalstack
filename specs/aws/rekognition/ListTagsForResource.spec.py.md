---
id: "@specs/aws/rekognition/list_tags_for_resource"
target_lang: py
version: 1.0.0
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/rekognition/plan"
---

# ListTagsForResource

Returns a list of tags in an Amazon Rekognition collection, stream processor, or Custom Labels model. This operation requires permissions to perform the rekognition:ListTagsForResource action.

## Input Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ResourceArn` | ResourceArn | Yes | Amazon Resource Name (ARN) of the model, collection, or stream processor that contains the tags that |

## Errors
- `AccessDeniedException`
- `InternalServerError`
- `InvalidParameterException`
- `ProvisionedThroughputExceededException`
- `ResourceNotFoundException`
- `ThrottlingException`

## Output Members
- `Tags`

## Implementation

```speclang
@dataclass
@kind: operation
def execute_list_tags_for_resource(store, request):
    """Returns a list of tags in an Amazon Rekognition collection, stream processor, or Custom Labels model. This operation requires permissions to perform the rekognition:ListTagsForResource action."""
    if not request.get("ResourceArn"):
        raise InvalidParameterException(f"{fname} is required")
    resource_arn = request["ResourceArn"]
    tags = store.tags.get(resource_arn, {})
    return {"Tags": tags}
```
