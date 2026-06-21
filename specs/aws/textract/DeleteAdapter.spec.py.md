---
id: "@specs/aws/textract/DeleteAdapter"
version: 1.0.0
target_lang: py
model_pool: code-gen
owned-by: codegen
status: active
---

# DeleteAdapter

## Implementation

```speclang
def execute_delete_adapter(store, request: dict) -> dict:
    adapter_id = request.get("AdapterId")
    if not adapter_id:
        raise InvalidParameterException("AdapterId is required")
    store.delete_adapter(adapter_id)
    return {}
```
