// spec:trace spec=/home/kara/totalstack/specs/aws/textract/StartLendingAnalysis.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

import uuid

def execute_start_lending_analysis(store, request: dict) -> dict:
    doc_location = request.get("DocumentLocation")
    if not doc_location:
        raise InvalidParameterException("DocumentLocation is required")

    job_id = str(uuid.uuid4())
    record = JobRecord(
        job_id=job_id,
        api="StartLendingAnalysis",
        document_location=doc_location,
        notification_channel=request.get("NotificationChannel"),
        output_config=request.get("OutputConfig"),
        client_request_token=request.get("ClientRequestToken"),
        kms_key_id=request.get("KMSKeyId"),
    )
    store.put_job(record)
    record.status = "SUCCEEDED"
    return {"JobId": job_id}

def execute_get_lending_analysis(store, request: dict) -> dict:
    job_id = request.get("JobId")
    if not job_id:
        raise InvalidParameterException("JobId is required")
    job = store.get_job(job_id)

    max_results = min(request.get("MaxResults", 1000), 1000)
    next_token = request.get("NextToken")

    results = [{"Page": 1, "PageClassification": {"PageType": [{"Value": "W2", "Confidence": 99.0}], "PageNumber": [{"Value": "1", "Confidence": 99.0}]},
                "Extractions": [{"LendingDocument": {"LendingFields": [
                    {"Type": "EMPLOYER_NAME", "ValueDetection": {"Text": "ACME Corp", "Confidence": 99.0}},
                    {"Type": "WAGES", "ValueDetection": {"Text": "$100,000", "Confidence": 99.0}},
                ]}}]}]

    start = int(next_token) if next_token else 0
    page = results[start:start + max_results]

    response = {
        "JobStatus": job.status,
        "DocumentMetadata": _build_document_metadata(),
        "Results": page,
    }
    if start + max_results < len(results):
        response["NextToken"] = str(start + max_results)
    return response

def execute_get_lending_analysis_summary(store, request: dict) -> dict:
    job_id = request.get("JobId")
    if not job_id:
        raise InvalidParameterException("JobId is required")
    job = store.get_job(job_id)

    return {
        "JobStatus": job.status,
        "DocumentMetadata": _build_document_metadata(),
        "Summary": {
            "DocumentGroups": [{"Type": "W2", "SplitDocuments": [
                {"Index": 0, "Pages": [1]}
            ]}],
        },
        "Warnings": [{"ErrorCode": "SIGNATURE_NOT_DETECTED", "Pages": [1]}],
        "StatusMessage": "OK",
        "AnalyzeLendingModelVersion": "1.0",
    }