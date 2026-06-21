---
id: "@specs/aws/athena/untag-resource"
version: 1.0.0
target_lang: py
output: specs/aws/.speclang/assembled/athena/UntagResource.code.py
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/athena/plan"
---
# UntagResource — Athena

Removes tags from an Athena resource.

## Implementation

```speclang
def untag_resource(store: 'AthenaStore', request: dict) -> dict:
    """Untag an Athena resource."""
    arn = request.get('ResourceARN')
    keys = request.get('TagKeys', [])
    if not arn:
        raise InvalidRequestException('ResourceARN is required')
    if arn in store.tags:
        for k in keys:
            store.tags[arn].pop(k, None)
    return {}
```
