---
id: "@specs/aws/textract"
version: 1.0.0
target_lang: meta
owned-by: think-tank
status: active
depends_on:
  - "@specs/aws/project"
---

# Amazon Textract — Service Overview

## Why

Amazon Textract is AWS's machine-learning-powered document intelligence service that extracts printed text, handwriting, tables, forms, and structured data from scanned documents. It goes beyond simple OCR by understanding document structure — identifying key-value pairs, tables, checkboxes, signatures, and even answering natural language queries about document content.

Textract is a critical building block for document processing pipelines: invoice processing, identity verification, contract analysis, mortgage applications, medical forms, and any workflow involving scanned or photographed documents.

For TotalStack, Textract is a **greenfield service** — no existing LocalStack provider exists. We build it from scratch against the AWS API Reference, implementing the full API surface as documented in botocore's service-2.json model (25 operations).

## Architecture

Textract splits into two operational modes:

### Synchronous Operations (real-time, <10MB documents)
- `AnalyzeDocument` — Forms, Tables, Signatures, Queries, Layout
- `DetectDocumentText` — Text lines and words only (baseline OCR)
- `AnalyzeExpense` — Invoice/receipt line items
- `AnalyzeID` — Government ID parsing (driver's license, passport)

### Asynchronous Operations (batch, up to 500MB PDFs)
- `StartDocumentAnalysis` → `GetDocumentAnalysis` — Full analysis pipeline
- `StartDocumentTextDetection` → `GetDocumentTextDetection` — Text extraction pipeline
- `StartExpenseAnalysis` → `GetExpenseAnalysis` — Expense pipeline
- `StartLendingAnalysis` → `GetLendingAnalysis` + `GetLendingAnalysisSummary` — Lending pipeline

### Adapter Management (custom models)
- `CreateAdapter` / `CreateAdapterVersion` — Create custom document adapters
- `GetAdapter` / `GetAdapterVersion` — Read adapter metadata
- `DeleteAdapter` / `DeleteAdapterVersion` — Remove adapters
- `ListAdapters` / `ListAdapterVersions` — Enumerate adapters
- `UpdateAdapter` — Modify adapter configuration

### Resource Tagging
- `TagResource` / `UntagResource` / `ListTagsForResource` — Standard AWS tagging

## Protocol

Textract uses **JSON protocol** (`jsonVersion: 1.1`, `targetPrefix: Textract`). All operations are POST to `/` with `X-Amz-Target: Textract.{Operation}` header. This is the simplest AWS protocol — no XML, no query string encoding, just JSON-in/JSON-out.

## Input Document Model

All analysis operations accept a `Document` object:

```json
{
  "Document": {
    "Bytes": "base64-encoded-image-bytes",
    "S3Object": {
      "Bucket": "my-bucket",
      "Name": "document.pdf",
      "Version": "version-id (optional)"
    }
  }
}
```

Exactly one of `Bytes` or `S3Object` must be provided — this is enforced by the `InvalidParameterException` validation.

## Feature Types

| Feature | Description | Available In |
|---------|-------------|--------------|
| `TABLES` | Detect table structures with cells | AnalyzeDocument, StartDocumentAnalysis |
| `FORMS` | Detect key-value pairs | AnalyzeDocument, StartDocumentAnalysis |
| `QUERIES` | Answer natural language questions | AnalyzeDocument, StartDocumentAnalysis |
| `SIGNATURES` | Detect signature locations | AnalyzeDocument, StartDocumentAnalysis |
| `LAYOUT` | Document layout (paragraphs, titles, headers) | AnalyzeDocument, StartDocumentAnalysis |

## Output: Block Model

All analysis responses return a list of `Block` objects. Each Block has:
- `BlockType`: KEY_VALUE_SET, LINE, WORD, TABLE, CELL, SELECTION_ELEMENT, SIGNATURE, QUERY, QUERY_RESULT, PAGE, LAYOUT_*
- `Id`, `Confidence`, `Geometry` (bounding box + polygon)
- `Relationships`: Parent-child links between blocks
- `Page`: Page number for multi-page documents

## Error Model

- `InvalidParameterException` — Bad input (e.g., missing both Bytes and S3Object)
- `InvalidS3ObjectException` — Can't access S3 object
- `UnsupportedDocumentException` — Wrong format (not PNG/JPEG/PDF/TIFF)
- `DocumentTooLargeException` — Sync >10MB, Async >500MB
- `BadDocumentException` — Corrupt/unreadable document
- `AccessDeniedException` — IAM/authorization
- `ProvisionedThroughputExceededException` — Rate limit
- `InternalServerError` — Service error (retryable)
- `ThrottlingException` — Transient throttle (retryable)
- `HumanLoopQuotaExceededException` — A2I human review quota
- `ResourceNotFoundException` — Adapter/job not found
- `ConflictException` — Resource state conflict
- `LimitExceededException` — Quota exceeded
- `ServiceQuotaExceededException` — AWS quota exceeded
- `IdempotentParameterMismatchException` — ClientToken mismatch
- `ValidationException` — Generic validation

## Success Metrics

- All 25 operations have SpecLang specs
- Integration tests cover core sync ops (AnalyzeDocument, DetectDocumentText, AnalyzeExpense, AnalyzeID)
- Integration tests cover adapter CRUD (Create, Get, List, Delete)
- Integration tests cover async start/get pairs
- E2E tests validate full workflows via boto3
- Mock document processing returns realistic Block output for TABLES + FORMS + TEXT features
