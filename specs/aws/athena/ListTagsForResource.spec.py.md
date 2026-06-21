---
id: "@specs/aws/athena/list-tags-for-resource"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/ListTagsForResource.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# ListTagsForResource — Athena

Lists tags for an Athena resource.

## Implementation

```speclang
def list_tags_for_resource(store: 'AthenaStore', request: dict) -> dict:
    """List tags for an Athena resource."""
    arn = request.get('ResourceARN')
    if not arn:
        raise InvalidRequestException('ResourceARN is required')
    tags = store.tags.get(arn, {})
    return {'Tags': [{'Key': k, 'Value': v} for k, v in tags.items()]}
```
