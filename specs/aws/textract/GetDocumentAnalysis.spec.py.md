---
id: "@specs/aws/textract/GetDocumentAnalysis"
version: 1.0.0
target_lang: py
model_pool: code-gen
owned-by: codegen
status: active
---

# GetDocumentAnalysis

## Implementation

```speclang
def execute_get_document_analysis(store, request: dict) -> dict:
    job_id = request.get("JobId")
    if not job_id:
        raise InvalidParameterException("JobId is required")

    job = store.get_job(job_id)

    max_results = min(request.get("MaxResults", 1000), 1000)
    next_token = request.get("NextToken")

    blocks = _generate_mock_document_blocks(page_count=2)
    if "TABLES" in job.feature_types:
        blocks.extend(_generate_mock_table_blocks())
    if "FORMS" in job.feature_types:
        blocks.extend(_generate_mock_form_blocks())

    start = 0
    if next_token:
        try:
            start = int(next_token)
        except ValueError:
            start = 0
    page = blocks[start:start + max_results]

    response = {
        "JobStatus": job.status,
        "DocumentMetadata": _build_document_metadata(2),
        "Blocks": page,
    }
    if start + max_results < len(blocks):
        response["NextToken"] = str(start + max_results)
    return response
```
