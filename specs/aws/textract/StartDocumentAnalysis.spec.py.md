---
id: "@specs/aws/textract/StartDocumentAnalysis"
version: 1.0.0
target_lang: py
model_pool: code-gen
owned-by: codegen
status: active
---

# StartDocumentAnalysis

## Implementation

```speclang
import uuid

def execute_start_document_analysis(store, request: dict) -> dict:
    doc_location = request.get("DocumentLocation", {})
    feature_types = request.get("FeatureTypes", [])

    if not doc_location:
        raise InvalidParameterException("DocumentLocation is required")
    if not feature_types:
        raise InvalidParameterException("FeatureTypes is required")

    valid_features = {"TABLES", "FORMS", "QUERIES", "SIGNATURES", "LAYOUT"}
    for ft in feature_types:
        if ft not in valid_features:
            raise InvalidParameterException(f"Invalid FeatureType: {ft}")

    client_token = request.get("ClientRequestToken")
    if client_token:
        for j in store.jobs.values():
            if j.client_request_token == client_token and j.api == "StartDocumentAnalysis":
                return {"JobId": j.job_id}

    job_id = str(uuid.uuid4())
    record = JobRecord(
        job_id=job_id,
        api="StartDocumentAnalysis",
        document_location=doc_location,
        feature_types=feature_types,
        notification_channel=request.get("NotificationChannel"),
        output_config=request.get("OutputConfig"),
        client_request_token=client_token,
        kms_key_id=request.get("KMSKeyId"),
        job_tag=request.get("JobTag"),
    )
    store.put_job(record)

    # Auto-complete async jobs immediately in local dev mode
    record.status = "SUCCEEDED"

    return {"JobId": job_id}
```
