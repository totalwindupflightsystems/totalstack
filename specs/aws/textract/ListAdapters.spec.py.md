---
id: "@specs/aws/textract/ListAdapters"
version: 1.0.0
target_lang: py
model_pool: code-gen
owned-by: codegen
status: active
---

# ListAdapters

## Implementation

```speclang
def execute_list_adapters(store, request: dict) -> dict:
    max_results = min(request.get("MaxResults", 1000), 1000)
    next_token = request.get("NextToken")
    return store.list_adapters(max_results=max_results, next_token=next_token)
```
