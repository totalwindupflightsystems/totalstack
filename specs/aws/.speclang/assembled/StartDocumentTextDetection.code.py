// spec:trace spec=/home/kara/totalstack/specs/aws/textract/StartDocumentTextDetection.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

import uuid

def execute_start_document_text_detection(store, request: dict) -> dict:
    doc_location = request.get("DocumentLocation")
    if not doc_location:
        raise InvalidParameterException("DocumentLocation is required")

    client_token = request.get("ClientRequestToken")
    if client_token:
        for j in store.jobs.values():
            if j.client_request_token == client_token and j.api == "StartDocumentTextDetection":
                return {"JobId": j.job_id}

    job_id = str(uuid.uuid4())
    record = JobRecord(
        job_id=job_id,
        api="StartDocumentTextDetection",
        document_location=doc_location,
        notification_channel=request.get("NotificationChannel"),
        output_config=request.get("OutputConfig"),
        client_request_token=client_token,
        kms_key_id=request.get("KMSKeyId"),
        job_tag=request.get("JobTag"),
    )
    store.put_job(record)
    record.status = "SUCCEEDED"
    return {"JobId": job_id}