---
id: "@specs/aws/textract/DetectDocumentText"
version: 1.0.0
target_lang: py
model_pool: code-gen
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/textract/plan"
  - "@specs/aws/textract/models"
---

# DetectDocumentText

Synchronous OCR — text lines and words only.

## Implementation

```speclang
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
```
