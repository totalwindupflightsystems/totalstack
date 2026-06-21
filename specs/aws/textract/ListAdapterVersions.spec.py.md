---
id: "@specs/aws/textract/ListAdapterVersions"
version: 1.0.0
target_lang: py
model_pool: code-gen
owned-by: codegen
status: active
---

# ListAdapterVersions

## Implementation

```speclang
def execute_list_adapter_versions(store, request: dict) -> dict:
    adapter_id = request.get("AdapterId")
    if adapter_id:
        a = store.get_adapter(adapter_id)
        versions = sorted(a.versions.keys())
    else:
        versions = []
        for aid in sorted(store.adapters.keys()):
            a = store.adapters[aid]
            versions.extend(f"{aid}/{v}" for v in sorted(a.versions.keys()))

    max_results = min(request.get("MaxResults", 1000), 1000)
    next_token = request.get("NextToken")
    start = int(next_token) if next_token else 0
    page = versions[start:start + max_results]

    result = {
        "AdapterVersions": [{"AdapterVersion": v, "CreationTime": time.time()} for v in page],
    }
    if start + max_results < len(versions):
        result["NextToken"] = str(start + max_results)
    return result
```
