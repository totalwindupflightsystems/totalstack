---
id: "@specs/aws/textract/AnalyzeID"
version: 1.0.0
target_lang: py
model_pool: code-gen
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/textract/plan"
  - "@specs/aws/textract/models"
---

# AnalyzeID

Synchronous identity document analysis — driver's license, passport.

## Implementation

```speclang
def execute_analyze_id(store, request: dict) -> dict:
    document_pages = request.get("DocumentPages", [])
    if not document_pages:
        raise InvalidParameterException(
            "DocumentPages is required"
        )

    identity_docs = []
    for dp in document_pages:
        doc = dp.get("Document", {})
        if not doc.get("Bytes") and not doc.get("S3Object"):
            raise InvalidParameterException(
                "Each DocumentPage must provide either Bytes or S3Object"
            )
        identity_docs.extend(_generate_mock_id_documents())

    return {
        "DocumentMetadata": _build_document_metadata(),
        "IdentityDocuments": identity_docs,
    }
```
