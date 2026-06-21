---
id: "@specs/aws/athena/tag-resource"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/TagResource.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# TagResource — Athena

Adds tags to an Athena resource.

## Implementation

```speclang
def tag_resource(store: 'AthenaStore', request: dict) -> dict:
    """Tag an Athena resource."""
    arn = request.get('ResourceARN')
    tags = request.get('Tags', [])
    if not arn:
        raise InvalidRequestException('ResourceARN is required')
    if arn not in store.tags:
        store.tags[arn] = {}
    for t in tags:
        store.tags[arn][t['Key']] = t['Value']
    return {}
```
