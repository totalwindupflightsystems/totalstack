---
id: "@specs/aws/textract/CreateAdapter"
version: 1.0.0
target_lang: py
model_pool: code-gen
owned-by: codegen
status: active
---

# CreateAdapter

## Implementation

```speclang
import uuid

def execute_create_adapter(store, request: dict) -> dict:
    adapter_name = request.get("AdapterName")
    feature_types = request.get("FeatureTypes", [])
    if not adapter_name:
        raise InvalidParameterException("AdapterName is required")
    if not feature_types:
        raise InvalidParameterException("FeatureTypes is required")

    valid_features = {"TABLES", "FORMS", "QUERIES", "SIGNATURES", "LAYOUT"}
    for ft in feature_types:
        if ft not in valid_features:
            raise InvalidParameterException(f"Invalid FeatureType: {ft}")

    adapter_id = str(uuid.uuid4())
    record = AdapterRecord(
        adapter_id=adapter_id,
        adapter_name=adapter_name,
        feature_types=feature_types,
        description=request.get("Description", ""),
        auto_update=request.get("AutoUpdate", "DISABLED"),
    )
    store.put_adapter(record)

    tags = request.get("Tags", {})
    if tags:
        arn = f"arn:aws:textract:us-east-1:000000000000:adapter/{adapter_id}"
        store.tag_resource(arn, {t["Key"]: t["Value"] for t in tags})

    return {"AdapterId": adapter_id}
```
