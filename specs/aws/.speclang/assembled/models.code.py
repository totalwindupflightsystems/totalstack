// spec:trace spec=/home/kara/totalstack/specs/aws/textract/models.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

"""Amazon Textract store and exception models for TotalStack."""
import time
import uuid
from dataclasses import dataclass, field
from typing import Any


# ── Exception Classes ─────────────────────────────────────────────

class AmazonTextractException(Exception):
    """Base exception for all Textract errors."""
    status_code: int = 400

class InvalidParameterException(AmazonTextractException):
    """An input parameter violated a constraint."""
    pass

class InvalidS3ObjectException(AmazonTextractException):
    """Unable to access the specified S3 object."""
    pass

class UnsupportedDocumentException(AmazonTextractException):
    """Document format not supported (must be PNG, JPEG, PDF, or TIFF)."""
    pass

class DocumentTooLargeException(AmazonTextractException):
    """Document exceeds size limits (sync: 10MB, async: 500MB)."""
    pass

class BadDocumentException(AmazonTextractException):
    """Document is corrupt or unreadable."""
    pass

class AccessDeniedException(AmazonTextractException):
    """Not authorized to perform this operation."""
    pass

class ProvisionedThroughputExceededException(AmazonTextractException):
    """Request rate exceeded throughput limit."""
    pass

class InternalServerException(AmazonTextractException):
    """Internal service error (retryable)."""
    status_code: int = 500

class ThrottlingException(AmazonTextractException):
    """Service temporarily throttled (retryable)."""
    pass

class HumanLoopQuotaExceededException(AmazonTextractException):
    """Maximum active human loop workflows exceeded."""
    pass

class ResourceNotFoundException(AmazonTextractException):
    """The requested resource (adapter, job) does not exist."""
    pass

class ConflictException(AmazonTextractException):
    """Resource state conflict."""
    pass

class LimitExceededException(AmazonTextractException):
    """A service quota was exceeded."""
    pass

class ServiceQuotaExceededException(AmazonTextractException):
    """AWS service quota exceeded."""
    pass

class IdempotentParameterMismatchException(AmazonTextractException):
    """ClientRequestToken mismatch on retry."""
    pass

class ValidationException(AmazonTextractException):
    """Generic validation failure."""
    pass


# ── Data Models ────────────────────────────────────────────────────

class AdapterVersionRecord:
    adapter_version: str
    creation_time: float
    status: str = "CREATING"  # CREATING | ACTIVE | FAILED
    evaluation_result: str = ""
    feature_types: list[str] = field(default_factory=list)
    tags: dict[str, str] = field(default_factory=dict)

class AdapterRecord:
    adapter_id: str
    adapter_name: str
    feature_types: list[str] = field(default_factory=list)
    creation_time: float = field(default_factory=time.time)
    auto_update: str = "DISABLED"
    description: str = ""
    status: str = "ACTIVE"
    versions: dict[str, AdapterVersionRecord] = field(default_factory=dict)

class JobRecord:
    job_id: str
    api: str  # StartDocumentAnalysis | StartDocumentTextDetection | StartExpenseAnalysis | StartLendingAnalysis
    status: str = "IN_PROGRESS"  # IN_PROGRESS | SUCCEEDED | FAILED | PARTIAL_SUCCESS
    document_location: dict = field(default_factory=dict)
    feature_types: list[str] = field(default_factory=list)
    created: float = field(default_factory=time.time)
    notification_channel: dict | None = None
    output_config: dict | None = None
    client_request_token: str | None = None
    job_tag: str | None = None
    kms_key_id: str | None = None


# ── Mock Document Processing ──────────────────────────────────────

def _make_block(block_type: str, block_id: str, page: int = 1,
                text: str = "", confidence: float = 99.0,
                relationships: list[dict] | None = None,
                geometry: dict | None = None,
                entity_types: list[str] | None = None,
                selection_status: str | None = None,
                row_index: int | None = None,
                column_index: int | None = None,
                row_span: int | None = None,
                column_span: int | None = None,
                query: dict | None = None) -> dict:
    """Build a Block dict matching AWS Textract output format."""
    block: dict[str, Any] = {
        "BlockType": block_type,
        "Id": block_id,
        "Confidence": confidence,
        "Geometry": geometry or {
            "BoundingBox": {"Width": 0.5, "Height": 0.02, "Left": 0.1, "Top": 0.1 * page},
            "Polygon": [
                {"X": 0.1, "Y": 0.1 * page},
                {"X": 0.6, "Y": 0.1 * page},
                {"X": 0.6, "Y": 0.12 * page},
                {"X": 0.1, "Y": 0.12 * page},
            ]
        },
        "Page": page,
    }
    if text:
        block["Text"] = text
    if relationships:
        block["Relationships"] = relationships
    if entity_types:
        block["EntityTypes"] = entity_types
    if selection_status:
        block["SelectionStatus"] = selection_status
    if row_index is not None:
        block["RowIndex"] = row_index
    if column_index is not None:
        block["ColumnIndex"] = column_index
    if row_span is not None:
        block["RowSpan"] = row_span
    if column_span is not None:
        block["ColumnSpan"] = column_span
    if query:
        block["Query"] = query
    return block


def _make_word(block_id: str, text: str, page: int = 1,
               child_of: str | None = None) -> dict:
    """Build a WORD block with optional parent relationship."""
    rels = None
    if child_of:
        rels = [{"Type": "CHILD", "Ids": []}]
        rels = [{"Type": "CHILD", "Ids": [block_id]}]
    b = _make_block("WORD", block_id, page, text, 99.0,
                    relationships=[{"Type": "CHILD", "Ids": [child_of]}] if child_of else None)
    return b


def _make_line(block_id: str, text: str, page: int = 1,
               word_ids: list[str] | None = None) -> dict:
    """Build a LINE block with child WORD relationships."""
    rels = None
    if word_ids:
        rels = [{"Type": "CHILD", "Ids": word_ids}]
    return _make_block("LINE", block_id, page, text, 99.0, relationships=rels)


def _generate_mock_document_blocks(page_count: int = 1) -> list[dict]:
    """Generate realistic mock blocks for a document with text."""
    blocks = []
    for page in range(1, page_count + 1):
        page_id = f"page-{page}"
        blocks.append(_make_block("PAGE", page_id, page))
        words = [
            ("This", "is", "a", "sample", "document", "page", f"number_{page}"),
        ]
        idx = 0
        for line_words in words:
            word_ids = []
            line_text = ""
            for w in line_words:
                wid = f"w-{idx}"
                word_ids.append(wid)
                blocks.append(_make_word(wid, w, page, child_of=f"l-{idx}"))
                if line_text:
                    line_text += " "
                line_text += w
                idx += 1
            blocks.append(_make_line(f"l-{idx}", line_text, page, word_ids))
            idx += 1
    return blocks


def _generate_mock_expense_documents() -> list[dict]:
    """Generate mock expense (invoice) blocks."""
    return [{
        "ExpenseIndex": 0,
        "SummaryFields": [
            {"Type": {"Text": "VENDOR_NAME", "Confidence": 99.0},
             "ValueDetection": {"Text": "ACME Corp", "Confidence": 99.0}},
            {"Type": {"Text": "TOTAL", "Confidence": 99.0},
             "ValueDetection": {"Text": "$1,234.56", "Confidence": 99.0}},
            {"Type": {"Text": "INVOICE_DATE", "Confidence": 99.0},
             "ValueDetection": {"Text": "2024-01-15", "Confidence": 99.0}},
            {"Type": {"Text": "TAX", "Confidence": 99.0},
             "ValueDetection": {"Text": "$123.46", "Confidence": 99.0}},
        ],
        "LineItemGroups": [{
            "LineItems": [
                {"LineItemExpenseFields": [
                    {"Type": {"Text": "ITEM", "Confidence": 99.0},
                     "ValueDetection": {"Text": "Widget A", "Confidence": 99.0}},
                    {"Type": {"Text": "QUANTITY", "Confidence": 99.0},
                     "ValueDetection": {"Text": "2", "Confidence": 99.0}},
                    {"Type": {"Text": "PRICE", "Confidence": 99.0},
                     "ValueDetection": {"Text": "$99.99", "Confidence": 99.0}},
                ]}
            ]
        }]
    }]


def _generate_mock_id_documents() -> list[dict]:
    """Generate mock identity document fields."""
    return [{
        "IdentityDocumentIndex": 0,
        "IdentityDocumentFields": [
            {"Type": {"Text": "FIRST_NAME"}, "ValueDetection": {"Text": "JOHN", "Confidence": 98.0}},
            {"Type": {"Text": "LAST_NAME"}, "ValueDetection": {"Text": "DOE", "Confidence": 98.0}},
            {"Type": {"Text": "DOCUMENT_NUMBER"}, "ValueDetection": {"Text": "DL-12345678", "Confidence": 97.0}},
            {"Type": {"Text": "DATE_OF_BIRTH"}, "ValueDetection": {"Text": "01/15/1985", "Confidence": 96.0}},
            {"Type": {"Text": "DATE_OF_EXPIRATION"}, "ValueDetection": {"Text": "01/15/2028", "Confidence": 95.0}},
        ]
    }]


def _generate_mock_form_blocks() -> list[dict]:
    """Generate mock KEY_VALUE_SET blocks."""
    return [
        _make_block("KEY_VALUE_SET", "kv-key-0", 1, entity_types=["KEY"],
                    relationships=[{"Type": "CHILD", "Ids": ["w-name"]},
                                   {"Type": "VALUE", "Ids": ["kv-val-0"]}]),
        _make_block("KEY_VALUE_SET", "kv-val-0", 1, entity_types=["VALUE"],
                    relationships=[{"Type": "CHILD", "Ids": ["w-john"]}]),
        _make_word("w-name", "Name:", 1, child_of="kv-key-0"),
        _make_word("w-john", "John Doe", 1, child_of="kv-val-0"),
        _make_block("KEY_VALUE_SET", "kv-key-1", 1, entity_types=["KEY"],
                    relationships=[{"Type": "CHILD", "Ids": ["w-date"]},
                                   {"Type": "VALUE", "Ids": ["kv-val-1"]}]),
        _make_block("KEY_VALUE_SET", "kv-val-1", 1, entity_types=["VALUE"],
                    relationships=[{"Type": "CHILD", "Ids": ["w-2024"]}]),
        _make_word("w-date", "Date:", 1, child_of="kv-key-1"),
        _make_word("w-2024", "01/15/2024", 1, child_of="kv-val-1"),
    ]


def _generate_mock_table_blocks() -> list[dict]:
    """Generate mock TABLE + CELL blocks."""
    cell_00 = _make_block("CELL", "cell-00", 1, row_index=1, column_index=1,
                          relationships=[{"Type": "CHILD", "Ids": ["w-h1"]}])
    cell_01 = _make_block("CELL", "cell-01", 1, row_index=1, column_index=2,
                          relationships=[{"Type": "CHILD", "Ids": ["w-h2"]}])
    cell_10 = _make_block("CELL", "cell-10", 1, row_index=2, column_index=1,
                          relationships=[{"Type": "CHILD", "Ids": ["w-d1"]}])
    cell_11 = _make_block("CELL", "cell-11", 1, row_index=2, column_index=2,
                          relationships=[{"Type": "CHILD", "Ids": ["w-d2"]}])
    table = _make_block("TABLE", "table-0", 1,
                        relationships=[{"Type": "CHILD", "Ids": ["cell-00", "cell-01", "cell-10", "cell-11"]}])
    return [table, cell_00, cell_01, cell_10, cell_11,
            _make_word("w-h1", "Name", 1, child_of="cell-00"),
            _make_word("w-h2", "Value", 1, child_of="cell-01"),
            _make_word("w-d1", "Foo", 1, child_of="cell-10"),
            _make_word("w-d2", "42", 1, child_of="cell-11")]


def _build_document_metadata(pages: int = 1) -> dict:
    return {"Pages": pages}


# ── Store ─────────────────────────────────────────────────────────

class TextractStore:
    """In-memory store for Textract resources."""

    def __init__(self):
        self.adapters: dict[str, AdapterRecord] = {}
        self.jobs: dict[str, JobRecord] = {}
        self.tags: dict[str, dict[str, str]] = {}

    def put_job(self, record: JobRecord) -> None:
        self.jobs[record.job_id] = record

    def get_job(self, job_id: str) -> JobRecord:
        if job_id not in self.jobs:
            raise ResourceNotFoundException(
                f"Job {job_id} not found"
            )
        return self.jobs[job_id]

    def put_adapter(self, record: AdapterRecord) -> None:
        self.adapters[record.adapter_id] = record

    def get_adapter(self, adapter_id: str) -> AdapterRecord:
        if adapter_id not in self.adapters:
            raise ResourceNotFoundException(
                f"Adapter {adapter_id} not found"
            )
        return self.adapters[adapter_id]

    def delete_adapter(self, adapter_id: str) -> None:
        if adapter_id not in self.adapters:
            raise ResourceNotFoundException(
                f"Adapter {adapter_id} not found"
            )
        del self.adapters[adapter_id]

    def list_adapters(self, max_results: int = 1000, next_token: str | None = None) -> dict:
        adapter_ids = sorted(self.adapters.keys())
        start = 0
        if next_token:
            try:
                start = int(next_token)
            except ValueError:
                start = 0
        page = adapter_ids[start:start + max_results]
        result = {
            "Adapters": [self._adapter_overview(aid) for aid in page],
        }
        if start + max_results < len(adapter_ids):
            result["NextToken"] = str(start + max_results)
        return result

    def _adapter_overview(self, adapter_id: str) -> dict:
        a = self.adapters[adapter_id]
        return {
            "AdapterId": a.adapter_id,
            "AdapterName": a.adapter_name,
            "FeatureTypes": a.feature_types,
            "CreationTime": a.creation_time,
            "Status": a.status,
        }

    def tag_resource(self, resource_arn: str, tags: dict[str, str]) -> None:
        if resource_arn not in self.tags:
            self.tags[resource_arn] = {}
        self.tags[resource_arn].update(tags)

    def untag_resource(self, resource_arn: str, tag_keys: list[str]) -> None:
        if resource_arn in self.tags:
            for k in tag_keys:
                self.tags[resource_arn].pop(k, None)

    def list_tags(self, resource_arn: str) -> dict[str, str]:
        return self.tags.get(resource_arn, {})