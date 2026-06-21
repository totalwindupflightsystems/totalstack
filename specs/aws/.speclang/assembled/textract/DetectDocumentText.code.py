# spec:trace: aws/textract/DetectDocumentText.spec.py.md#implementation
# spec:id: @specs/aws/textract/detectdocumenttext
# spec:generated: DO NOT EDIT — edit the spec instead

def execute_detect_document_text(store, request: dict) -> dict:
    doc = request.get("Document", {})
    has_bytes = "Bytes" in doc
    has_s3 = "S3Object" in doc
    if not has_bytes and not has_s3:
        raise InvalidParameterException(
            "Document must provide either Bytes or S3Object"
        )
    if has_bytes and has_s3:
        raise InvalidParameterException(
            "Document cannot provide both Bytes and S3Object"
        )

    blocks = _generate_mock_document_blocks(page_count=1)
    return {
        "DocumentMetadata": _build_document_metadata(),
        "Blocks": blocks,
        "DetectDocumentTextModelVersion": "1.0",
    }

