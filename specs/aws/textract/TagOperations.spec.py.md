---
id: "@specs/aws/textract/TagOperations"
version: 1.0.0
target_lang: py
model_pool: code-gen
owned-by: codegen
status: active
---

# TagResource / UntagResource / ListTagsForResource

## Implementation

```speclang
def execute_tag_resource(store, request: dict) -> dict:
    resource_arn = request.get("ResourceARN")
    tags = request.get("Tags", [])
    if not resource_arn:
        raise InvalidParameterException("ResourceARN is required")
    if not tags:
        raise InvalidParameterException("Tags is required")
    store.tag_resource(resource_arn, {t["Key"]: t["Value"] for t in tags})
    return {}

def execute_untag_resource(store, request: dict) -> dict:
    resource_arn = request.get("ResourceARN")
    tag_keys = request.get("TagKeys", [])
    if not resource_arn:
        raise InvalidParameterException("ResourceARN is required")
    if not tag_keys:
        raise InvalidParameterException("TagKeys is required")
    store.untag_resource(resource_arn, tag_keys)
    return {}

def execute_list_tags_for_resource(store, request: dict) -> dict:
    resource_arn = request.get("ResourceARN")
    if not resource_arn:
        raise InvalidParameterException("ResourceARN is required")
    tags = store.list_tags(resource_arn)
    return {"Tags": [{"Key": k, "Value": v} for k, v in tags.items()]}
```
