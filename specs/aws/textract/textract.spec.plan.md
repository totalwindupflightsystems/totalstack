---
id: "@specs/aws/textract/plan"
version: 1.0.0
target_lang: plan
owned-by: think-tank
status: active
depends_on:
  - "@specs/aws/textract"
---

# Textract Implementation Plan

## Operations (25 total)

### Synchronous Analysis (4 ops)
| Operation | Method | Required Fields | Return Type |
|-----------|--------|----------------|-------------|
| AnalyzeDocument | POST | Document, FeatureTypes | List<Block> + DocumentMetadata |
| DetectDocumentText | POST | Document | List<Block> + DocumentMetadata |
| AnalyzeExpense | POST | Document | List<ExpenseDocument> + DocumentMetadata |
| AnalyzeID | POST | DocumentPages | List<IdentityDocument> + DocumentMetadata |

### Asynchronous Analysis (7 ops)
| Operation | Method | Required Fields | Return Type |
|-----------|--------|----------------|-------------|
| StartDocumentAnalysis | POST | DocumentLocation, FeatureTypes | JobId |
| GetDocumentAnalysis | POST | JobId | JobStatus + List<Block> + pagination |
| StartDocumentTextDetection | POST | DocumentLocation | JobId |
| GetDocumentTextDetection | POST | JobId | JobStatus + List<Block> + pagination |
| StartExpenseAnalysis | POST | DocumentLocation | JobId |
| GetExpenseAnalysis | POST | JobId | JobStatus + List<ExpenseDocument> |
| StartLendingAnalysis | POST | DocumentLocation | JobId |
| GetLendingAnalysis | POST | JobId | JobStatus + List<LendingResult> |
| GetLendingAnalysisSummary | POST | JobId | Summary + signature detection |

### Adapter Management (9 ops)
| Operation | Method | Required Fields | Return Type |
|-----------|--------|----------------|-------------|
| CreateAdapter | POST | AdapterName, FeatureTypes | AdapterId |
| CreateAdapterVersion | POST | AdapterId, DatasetConfig, OutputConfig | AdapterVersion |
| GetAdapter | POST | AdapterId | Adapter metadata |
| GetAdapterVersion | POST | AdapterId, AdapterVersion | AdapterVersion metadata |
| DeleteAdapter | POST | AdapterId | (empty) |
| DeleteAdapterVersion | POST | AdapterId, AdapterVersion | (empty) |
| ListAdapters | POST | (none — pagination only) | List<AdapterOverview> |
| ListAdapterVersions | POST | AdapterId (optional) | List<AdapterVersionOverview> |
| UpdateAdapter | POST | AdapterId | Adapter metadata (updated) |

### Tagging (3 ops)
| Operation | Method | Required Fields | Return Type |
|-----------|--------|----------------|-------------|
| TagResource | POST | ResourceARN, Tags | (empty) |
| UntagResource | POST | ResourceARN, TagKeys | (empty) |
| ListTagsForResource | POST | ResourceARN | Tags list |

## Store Design

### Main Store
```python
class TextractStore:
    adapters: dict[str, AdapterRecord]       # AdapterId → AdapterRecord
    jobs: dict[str, JobRecord]               # JobId → JobRecord
    tags: dict[str, dict[str, str]]          # ResourceARN → {key: value}
```

### AdapterRecord
```python
@dataclass
class AdapterRecord:
    adapter_id: str
    adapter_name: str
    feature_types: list[str]
    creation_time: float
    auto_update: str  # ENABLED | DISABLED
    description: str
    versions: dict[str, AdapterVersionRecord]
    status: str  # ACTIVE | CREATING | DELETING
```

### JobRecord
```python
@dataclass  
class JobRecord:
    job_id: str
    api: str  # StartDocumentAnalysis | StartDocumentTextDetection | etc.
    status: str  # IN_PROGRESS | SUCCEEDED | FAILED | PARTIAL_SUCCESS
    document_location: dict
    feature_types: list[str]  # for analysis jobs
    created: float
    notification_channel: dict | None
    output_config: dict | None
    client_request_token: str | None
    job_tag: str | None  # for expense/lending
```

## Exception Classes

```python
class AmazonTextractException(Exception): ...
class InvalidParameterException(AmazonTextractException): ...
class InvalidS3ObjectException(AmazonTextractException): ...
class UnsupportedDocumentException(AmazonTextractException): ...
class DocumentTooLargeException(AmazonTextractException): ...
class BadDocumentException(AmazonTextractException): ...
class AccessDeniedException(AmazonTextractException): ...
class ProvisionedThroughputExceededException(AmazonTextractException): ...
class InternalServerException(AmazonTextractException): ...
class ThrottlingException(AmazonTextractException): ...
class HumanLoopQuotaExceededException(AmazonTextractException): ...
class ResourceNotFoundException(AmazonTextractException): ...
class ConflictException(AmazonTextractException): ...
class LimitExceededException(AmazonTextractException): ...
class ServiceQuotaExceededException(AmazonTextractException): ...
class IdempotentParameterMismatchException(AmazonTextractException): ...
class ValidationException(AmazonTextractException): ...
```

## Mock Document Processing

Since we're building a localstack emulator, we don't have access to Amazon's ML models. We provide **realistic mock responses**:

1. **DetectDocumentText**: Return synthetic LINE + WORD blocks with Lorem Ipsum text, varying per page count and document type
2. **AnalyzeDocument with FORMS**: Return KEY_VALUE_SET blocks with synthetic key-value pairs ("Name: John Doe", "Date: 01/15/2024")
3. **AnalyzeDocument with TABLES**: Return TABLE + CELL blocks in a synthetic grid
4. **AnalyzeExpense**: Return synthetic expense line items (vendor, total, tax, date)
5. **AnalyzeID**: Return synthetic identity fields (FIRST_NAME, LAST_NAME, DOB, DOCUMENT_NUMBER)
6. **Async jobs**: Transition IN_PROGRESS → SUCCEEDED after a configurable delay (default 2s)

## Protocol Implementation

JSON protocol: read `X-Amz-Target: Textract.{Operation}` header, dispatch to handler. All operations use POST / with JSON body.

## Pagination

Operations with pagination (GetDocumentAnalysis, GetDocumentTextDetection, ListAdapterVersions, ListAdapters):
- Accept `NextToken` as input
- Return `NextToken` in output when more pages exist
- MaxResults defaults to 1000
