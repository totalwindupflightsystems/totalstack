---
id: "@specs/aws/textract/StartExpenseAnalysis"
version: 1.0.0
target_lang: py
model_pool: code-gen
owned-by: codegen
status: active
---

# StartExpenseAnalysis / GetExpenseAnalysis

## Implementation

```speclang
import uuid

def execute_start_expense_analysis(store, request: dict) -> dict:
    doc_location = request.get("DocumentLocation")
    if not doc_location:
        raise InvalidParameterException("DocumentLocation is required")

    job_id = str(uuid.uuid4())
    record = JobRecord(
        job_id=job_id,
        api="StartExpenseAnalysis",
        document_location=doc_location,
        notification_channel=request.get("NotificationChannel"),
        output_config=request.get("OutputConfig"),
        client_request_token=request.get("ClientRequestToken"),
        kms_key_id=request.get("KMSKeyId"),
    )
    store.put_job(record)
    record.status = "SUCCEEDED"
    return {"JobId": job_id}

def execute_get_expense_analysis(store, request: dict) -> dict:
    job_id = request.get("JobId")
    if not job_id:
        raise InvalidParameterException("JobId is required")
    job = store.get_job(job_id)

    max_results = min(request.get("MaxResults", 1000), 1000)
    next_token = request.get("NextToken")

    expense_docs = _generate_mock_expense_documents()
    start = int(next_token) if next_token else 0
    page = expense_docs[start:start + max_results]

    response = {
        "JobStatus": job.status,
        "DocumentMetadata": _build_document_metadata(),
        "ExpenseDocuments": page,
    }
    if start + max_results < len(expense_docs):
        response["NextToken"] = str(start + max_results)
    return response
```
