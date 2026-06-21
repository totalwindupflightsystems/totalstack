---
id: "@specs/aws/textract/GetAdapterVersion"
version: 1.0.0
target_lang: py
model_pool: code-gen
owned-by: codegen
status: active
---

# GetAdapterVersion

## Implementation

```speclang
def execute_get_adapter_version(store, request: dict) -> dict:
    adapter_id = request.get("AdapterId")
    version = request.get("AdapterVersion")
    if not adapter_id or not version:
        raise InvalidParameterException("AdapterId and AdapterVersion are required")

    a = store.get_adapter(adapter_id)
    if version not in a.versions:
        raise ResourceNotFoundException(f"AdapterVersion {version} not found")

    v = a.versions[version]
    return {
        "AdapterId": adapter_id,
        "AdapterVersion": version,
        "CreationTime": v.creation_time,
        "Status": v.status,
        "FeatureTypes": v.feature_types,
        "EvaluationResult": v.evaluation_result,
    }
```
