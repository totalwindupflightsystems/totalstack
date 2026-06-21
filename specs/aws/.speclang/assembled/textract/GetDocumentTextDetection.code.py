# spec:trace: aws/textract/GetDocumentTextDetection.spec.py.md#implementation
# spec:id: @specs/aws/textract/getdocumenttextdetection
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_get_document_text_detection(store, request: dict) -> dict:
    job_id = request.get("JobId")
    if not job_id:
        raise InvalidParameterException("JobId is required")
    job = store.get_job(job_id)

    max_results = min(request.get("MaxResults", 1000), 1000)
    next_token = request.get("NextToken")

    blocks = _generate_mock_document_blocks(page_count=2)
    start = int(next_token) if next_token else 0
    page = blocks[start:start + max_results]

    response = {
        "JobStatus": job.status,
        "DocumentMetadata": _build_document_metadata(2),
        "Blocks": page,
    }
    if start + max_results < len(blocks):
        response["NextToken"] = str(start + max_results)
    return response

