"""Integration test for Textract — real TextractStore."""
import pytest
import os
import sys
import types
import importlib.util

# Path setup for greenfield service
ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'textract')
sys.path.insert(0, SERVICE_DIR)

# Import store, exceptions, and helpers from generated models
# Use importlib since models.py is in a dynamically-added path
models_spec = importlib.util.spec_from_file_location('models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out needed names
TextractStore = models_mod.TextractStore
AdapterRecord = models_mod.AdapterRecord
AdapterVersionRecord = models_mod.AdapterVersionRecord
JobRecord = models_mod.JobRecord
InvalidParameterException = models_mod.InvalidParameterException
ResourceNotFoundException = models_mod.ResourceNotFoundException
_generate_mock_document_blocks = models_mod._generate_mock_document_blocks
_generate_mock_table_blocks = models_mod._generate_mock_table_blocks
_generate_mock_form_blocks = models_mod._generate_mock_form_blocks
_generate_mock_expense_documents = models_mod._generate_mock_expense_documents
_generate_mock_id_documents = models_mod._generate_mock_id_documents
_make_block = models_mod._make_block
_build_document_metadata = models_mod._build_document_metadata


def _load_module(op_name, globals_inject=None):
    """Load a generated .code.py module (for multi-handler files)."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    return mod


def _load_handler(op_name, globals_inject=None):
    """Load a generated .code.py handler and inject required globals."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)

    # Inject exception classes and helpers that generated code references
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException

    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)

    spec.loader.exec_module(mod)

    # Find handler function (exclude imports like uuid, time)
    handler = None
    for v in mod.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_'):
            handler = v
            break
    return handler


class TestTextractDetectDocumentText:
    """Baseline OCR — text detection."""

    def test_happy_path(self):
        store = TextractStore()
        handler = _load_handler('DetectDocumentText', {
            '_generate_mock_document_blocks': _generate_mock_document_blocks,
            '_build_document_metadata': _build_document_metadata,
        })
        response = handler(store, {
            "Document": {"Bytes": "bW9ja2Jhc2U2NA=="}
        })
        assert "Blocks" in response
        assert "DocumentMetadata" in response
        assert len(response["Blocks"]) > 0
        assert response["Blocks"][0]["BlockType"] == "PAGE"

    def test_missing_document(self):
        store = TextractStore()
        handler = _load_handler('DetectDocumentText', {
            '_generate_mock_document_blocks': _generate_mock_document_blocks,
            '_build_document_metadata': _build_document_metadata,
        })
        with pytest.raises(InvalidParameterException, match="Document must provide"):
            handler(store, {"Document": {}})

    def test_s3_document(self):
        store = TextractStore()
        handler = _load_handler('DetectDocumentText', {
            '_generate_mock_document_blocks': _generate_mock_document_blocks,
            '_build_document_metadata': _build_document_metadata,
        })
        response = handler(store, {
            "Document": {"S3Object": {"Bucket": "test", "Name": "doc.pdf"}}
        })
        assert "Blocks" in response
        assert len(response["Blocks"]) > 0


class TestTextractAnalyzeDocument:
    """Full analysis with feature types."""

    def test_tables_feature(self):
        store = TextractStore()
        handler = _load_handler('AnalyzeDocument', {
            '_generate_mock_document_blocks': _generate_mock_document_blocks,
            '_generate_mock_table_blocks': _generate_mock_table_blocks,
            '_generate_mock_form_blocks': _generate_mock_form_blocks,
            '_make_block': _make_block,
            '_build_document_metadata': _build_document_metadata,
        })
        response = handler(store, {
            "Document": {"Bytes": "bW9jaw=="},
            "FeatureTypes": ["TABLES"]
        })
        block_types = [b["BlockType"] for b in response["Blocks"]]
        assert "TABLE" in block_types
        assert "CELL" in block_types

    def test_forms_feature(self):
        store = TextractStore()
        handler = _load_handler('AnalyzeDocument', {
            '_generate_mock_document_blocks': _generate_mock_document_blocks,
            '_generate_mock_table_blocks': _generate_mock_table_blocks,
            '_generate_mock_form_blocks': _generate_mock_form_blocks,
            '_make_block': _make_block,
            '_build_document_metadata': _build_document_metadata,
        })
        response = handler(store, {
            "Document": {"Bytes": "bW9jaw=="},
            "FeatureTypes": ["FORMS"]
        })
        block_types = [b["BlockType"] for b in response["Blocks"]]
        assert "KEY_VALUE_SET" in block_types

    def test_invalid_feature_type(self):
        store = TextractStore()
        handler = _load_handler('AnalyzeDocument', {
            '_generate_mock_document_blocks': _generate_mock_document_blocks,
            '_generate_mock_table_blocks': _generate_mock_table_blocks,
            '_generate_mock_form_blocks': _generate_mock_form_blocks,
            '_make_block': _make_block,
            '_build_document_metadata': _build_document_metadata,
        })
        with pytest.raises(InvalidParameterException, match="Invalid FeatureType"):
            handler(store, {
                "Document": {"Bytes": "bW9jaw=="},
                "FeatureTypes": ["INVALID"]
            })

    def test_missing_document(self):
        store = TextractStore()
        handler = _load_handler('AnalyzeDocument', {
            '_generate_mock_document_blocks': _generate_mock_document_blocks,
            '_generate_mock_table_blocks': _generate_mock_table_blocks,
            '_generate_mock_form_blocks': _generate_mock_form_blocks,
            '_make_block': _make_block,
            '_build_document_metadata': _build_document_metadata,
        })
        with pytest.raises(InvalidParameterException, match="Document must provide"):
            handler(store, {
                "Document": {},
                "FeatureTypes": ["TABLES"]
            })


class TestTextractAnalyzeExpense:
    """Expense analysis."""

    def test_happy_path(self):
        store = TextractStore()
        handler = _load_handler('AnalyzeExpense', {
            '_generate_mock_expense_documents': _generate_mock_expense_documents,
            '_build_document_metadata': _build_document_metadata,
        })
        response = handler(store, {
            "Document": {"Bytes": "bW9jaw=="}
        })
        assert "ExpenseDocuments" in response
        exp_docs = response["ExpenseDocuments"]
        assert len(exp_docs) > 0
        assert "SummaryFields" in exp_docs[0]
        # Check vendor name
        vendor_field = next(
            (f for f in exp_docs[0]["SummaryFields"]
             if f["Type"]["Text"] == "VENDOR_NAME"), None)
        assert vendor_field is not None
        assert vendor_field["ValueDetection"]["Text"] == "ACME Corp"


class TestTextractAnalyzeID:
    """Identity document analysis."""

    def test_happy_path(self):
        store = TextractStore()
        handler = _load_handler('AnalyzeID', {
            '_generate_mock_id_documents': _generate_mock_id_documents,
            '_build_document_metadata': _build_document_metadata,
        })
        response = handler(store, {
            "DocumentPages": [
                {"Document": {"Bytes": "bW9jaw=="}}
            ]
        })
        assert "IdentityDocuments" in response
        assert len(response["IdentityDocuments"]) > 0
        fields = response["IdentityDocuments"][0]["IdentityDocumentFields"]
        field_types = [f["Type"]["Text"] for f in fields]
        assert "FIRST_NAME" in field_types
        assert "LAST_NAME" in field_types


class TestTextractAdapterCRUD:
    """Adapter create, get, list, delete."""

    def test_create_adapter(self):
        store = TextractStore()
        import uuid
        globals_inject = {
            'uuid': uuid,
            'InvalidParameterException': InvalidParameterException,
            'ResourceNotFoundException': ResourceNotFoundException,
            'AdapterRecord': AdapterRecord,
        }
        handler = _load_handler('CreateAdapter', globals_inject)
        response = handler(store, {
            "AdapterName": "test-adapter",
            "FeatureTypes": ["TABLES", "FORMS"],
        })
        assert "AdapterId" in response
        adapter_id = response["AdapterId"]
        assert adapter_id in store.adapters
        assert store.adapters[adapter_id].adapter_name == "test-adapter"

    def test_get_adapter(self):
        store = TextractStore()
        store.put_adapter(AdapterRecord(
            adapter_id="test-id",
            adapter_name="test-adapter",
            feature_types=["TABLES"],
        ))
        handler = _load_handler('GetAdapter')
        response = handler(store, {"AdapterId": "test-id"})
        assert response["AdapterId"] == "test-id"
        assert response["AdapterName"] == "test-adapter"

    def test_get_nonexistent_adapter(self):
        store = TextractStore()
        handler = _load_handler('GetAdapter')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {"AdapterId": "nonexistent"})

    def test_delete_adapter(self):
        store = TextractStore()
        store.put_adapter(AdapterRecord(
            adapter_id="test-id",
            adapter_name="test-adapter",
            feature_types=["TABLES"],
        ))
        handler = _load_handler('DeleteAdapter')
        handler(store, {"AdapterId": "test-id"})
        assert "test-id" not in store.adapters

    def test_list_adapters(self):
        store = TextractStore()
        for i in range(3):
            store.put_adapter(AdapterRecord(
                adapter_id=f"id-{i}",
                adapter_name=f"adapter-{i}",
                feature_types=["TABLES"],
            ))
        handler = _load_handler('ListAdapters')
        response = handler(store, {})
        assert "Adapters" in response
        assert len(response["Adapters"]) == 3


class TestTextractAsyncJobs:
    """Start/get async document analysis."""

    def test_start_and_get_analysis(self):
        store = TextractStore()
        import uuid
        start_handler = _load_handler('StartDocumentAnalysis', {
            'uuid': uuid,
            'JobRecord': JobRecord,
        })
        start_resp = start_handler(store, {
            "DocumentLocation": {"S3Object": {"Bucket": "b", "Name": "doc.pdf"}},
            "FeatureTypes": ["TABLES", "FORMS"],
        })
        assert "JobId" in start_resp
        job_id = start_resp["JobId"]
        assert job_id in store.jobs
        assert store.jobs[job_id].status == "SUCCEEDED"

        get_handler = _load_handler('GetDocumentAnalysis', {
            '_generate_mock_document_blocks': _generate_mock_document_blocks,
            '_generate_mock_table_blocks': _generate_mock_table_blocks,
            '_generate_mock_form_blocks': _generate_mock_form_blocks,
            '_build_document_metadata': _build_document_metadata,
        })
        get_resp = get_handler(store, {"JobId": job_id})
        assert get_resp["JobStatus"] == "SUCCEEDED"
        assert "Blocks" in get_resp

    def test_get_nonexistent_job(self):
        store = TextractStore()
        handler = _load_handler('GetDocumentAnalysis')
        with pytest.raises(ResourceNotFoundException, match="not found"):
            handler(store, {"JobId": "nonexistent"})


class TestTextractTagging:
    """Resource tagging."""

    def test_tag_and_list(self):
        store = TextractStore()
        # Tag operations are combined in TagOperations.code.py
        tag_ops_mod = _load_module('TagOperations')
        tag_handler = tag_ops_mod.execute_tag_resource
        untag_handler = tag_ops_mod.execute_untag_resource
        list_handler = tag_ops_mod.execute_list_tags_for_resource

        tag_handler(store, {
            "ResourceARN": "arn:aws:textract:us-east-1:000000000000:adapter/test",
            "Tags": [{"Key": "env", "Value": "test"}, {"Key": "owner", "Value": "team"}]
        })
        tags = list_handler(store, {
            "ResourceARN": "arn:aws:textract:us-east-1:000000000000:adapter/test"
        })
        tag_dict = {t["Key"]: t["Value"] for t in tags["Tags"]}
        assert tag_dict["env"] == "test"
        assert tag_dict["owner"] == "team"

        untag_handler(store, {
            "ResourceARN": "arn:aws:textract:us-east-1:000000000000:adapter/test",
            "TagKeys": ["env"]
        })
        tags = list_handler(store, {
            "ResourceARN": "arn:aws:textract:us-east-1:000000000000:adapter/test"
        })
        tag_dict = {t["Key"]: t["Value"] for t in tags["Tags"]}
        assert "env" not in tag_dict
        assert tag_dict["owner"] == "team"


class TestTextractAdapterVersions:
    """Adapter version CRUD."""

    def test_create_and_get_version(self):
        store = TextractStore()
        store.put_adapter(AdapterRecord(
            adapter_id="adapter-1",
            adapter_name="test-adapter",
            feature_types=["TABLES"],
        ))
        import uuid, time
        create_handler = _load_handler('CreateAdapterVersion', {
            'uuid': uuid, 'time': time,
            'AdapterVersionRecord': AdapterVersionRecord,
        })
        resp = create_handler(store, {
            "AdapterId": "adapter-1",
            "DatasetConfig": {"ManifestS3Object": {"Bucket": "b", "Name": "m.csv"}},
            "OutputConfig": {"S3Bucket": "b", "S3Prefix": "out/"},
        })
        assert resp["AdapterId"] == "adapter-1"
        version = resp["AdapterVersion"]
        assert version in store.adapters["adapter-1"].versions

        get_handler = _load_handler('GetAdapterVersion')
        resp2 = get_handler(store, {"AdapterId": "adapter-1", "AdapterVersion": version})
        assert resp2["Status"] == "ACTIVE"

    def test_delete_version(self):
        store = TextractStore()
        a = AdapterRecord(adapter_id="adapter-1", adapter_name="test", feature_types=["TABLES"])
        a.versions["v1"] = AdapterVersionRecord(adapter_version="v1", creation_time=0, status="ACTIVE")
        store.put_adapter(a)

        handler = _load_handler('DeleteAdapterVersion')
        handler(store, {"AdapterId": "adapter-1", "AdapterVersion": "v1"})
        assert "v1" not in store.adapters["adapter-1"].versions
