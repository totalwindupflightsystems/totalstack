"""Integration test for ACM Certificate Manager — real ACMStore."""
import pytest
import os
import types
import importlib.util

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, "..", "acm")

# Load models
models_spec = importlib.util.spec_from_file_location(
    "models", os.path.join(SERVICE_DIR, "models.code.py"))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

ACMStore = models_mod.ACMStore
CertificateRecord = models_mod.CertificateRecord
InvalidParameterException = models_mod.InvalidParameterException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceInUseException = models_mod.ResourceInUseException
InvalidStateException = models_mod.InvalidStateException
LimitExceededException = models_mod.LimitExceededException
TooManyTagsException = models_mod.TooManyTagsException
InvalidTagException = models_mod.InvalidTagException
ValidationException = models_mod.ValidationException


skip_names = {"dataclass", "time", "uuid", "<lambda>", "datetime"}


def _load_handler(op_name, globals_inject=None):
    """Load a generated .code.py handler — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + ".code.py")
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ResourceInUseException = ResourceInUseException
    mod.InvalidStateException = InvalidStateException
    mod.LimitExceededException = LimitExceededException
    mod.TooManyTagsException = TooManyTagsException
    mod.InvalidTagException = InvalidTagException
    mod.ValidationException = ValidationException
    mod.CertificateRecord = CertificateRecord
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
            and not v.__name__.startswith("_")
            and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestACMCoreCRUD:
    """Request, describe, get, list, delete — core certificate lifecycle."""

    @pytest.fixture
    def store(self):
        return ACMStore()

    def test_request_certificate_happy(self, store):
        handler = _load_handler("request-certificate")
        resp = handler(store, {
            "DomainName": "example.com",
            "ValidationMethod": "EMAIL",
            "KeyAlgorithm": "RSA_2048",
        })
        assert "CertificateArn" in resp
        assert resp["CertificateArn"].startswith("arn:aws:acm:")

    def test_request_certificate_missing_domain(self, store):
        handler = _load_handler("request-certificate")
        with pytest.raises(KeyError):
            handler(store, {})

    def test_describe_certificate_happy(self, store):
        req_handler = _load_handler("request-certificate")
        resp = req_handler(store, {"DomainName": "example.com"})
        arn = resp["CertificateArn"]

        desc_handler = _load_handler("describe-certificate")
        result = desc_handler(store, {"CertificateArn": arn})
        assert "Certificate" in result
        assert result["Certificate"]["CertificateArn"] == arn
        assert result["Certificate"]["Status"] == "PENDING_VALIDATION"

    def test_describe_certificate_not_found(self, store):
        handler = _load_handler("describe-certificate")
        with pytest.raises(ResourceNotFoundException):
            handler(store, {"CertificateArn": "arn:aws:acm:us-east-1:000000000000:certificate/nonexistent"})

    def test_get_certificate_not_found(self, store):
        handler = _load_handler("get-certificate")
        with pytest.raises(ResourceNotFoundException):
            handler(store, {"CertificateArn": "arn:aws:acm:us-east-1:000000000000:certificate/nonexistent"})

    def test_get_certificate_not_issued(self, store):
        req_handler = _load_handler("request-certificate")
        resp = req_handler(store, {"DomainName": "example.com"})
        arn = resp["CertificateArn"]

        get_handler = _load_handler("get-certificate")
        with pytest.raises(InvalidStateException):
            get_handler(store, {"CertificateArn": arn})

    def test_list_certificates_empty(self, store):
        handler = _load_handler("list-certificates")
        result = handler(store, {})
        assert "CertificateSummaryList" in result
        assert len(result["CertificateSummaryList"]) == 0

    def test_list_certificates_with_entries(self, store):
        req_handler = _load_handler("request-certificate")
        req_handler(store, {"DomainName": "a.example.com"})
        req_handler(store, {"DomainName": "b.example.com"})

        list_handler = _load_handler("list-certificates")
        result = list_handler(store, {})
        assert len(result["CertificateSummaryList"]) == 2

    def test_delete_certificate_happy(self, store):
        req_handler = _load_handler("request-certificate")
        resp = req_handler(store, {"DomainName": "example.com"})
        arn = resp["CertificateArn"]

        del_handler = _load_handler("delete-certificate")
        del_handler(store, {"CertificateArn": arn})

        desc_handler = _load_handler("describe-certificate")
        with pytest.raises(ResourceNotFoundException):
            desc_handler(store, {"CertificateArn": arn})

    def test_delete_certificate_not_found(self, store):
        handler = _load_handler("delete-certificate")
        with pytest.raises(ResourceNotFoundException):
            handler(store, {"CertificateArn": "arn:aws:acm:us-east-1:000000000000:certificate/nonexistent"})


class TestACMImportExport:
    """Import and export certificate operations."""

    @pytest.fixture
    def store(self):
        return ACMStore()

    def test_import_certificate_happy(self, store):
        handler = _load_handler("import-certificate")
        resp = handler(store, {
            "Certificate": "-----BEGIN CERTIFICATE-----\ntest\n-----END CERTIFICATE-----",
            "PrivateKey": "-----BEGIN PRIVATE KEY-----\ntest\n-----END PRIVATE KEY-----",
        })
        assert "CertificateArn" in resp
        arn = resp["CertificateArn"]
        # Verify it's in the store
        desc_handler = _load_handler("describe-certificate")
        result = desc_handler(store, {"CertificateArn": arn})
        assert result["Certificate"]["Status"] == "ISSUED"

    def test_export_certificate_not_private(self, store):
        imp_handler = _load_handler("import-certificate")
        resp = imp_handler(store, {
            "Certificate": "test-cert",
            "PrivateKey": "test-key",
        })
        arn = resp["CertificateArn"]

        exp_handler = _load_handler("export-certificate")
        with pytest.raises(InvalidStateException):
            exp_handler(store, {"CertificateArn": arn, "Passphrase": b"test"})


class TestACMTags:
    """Tag add/list/remove operations."""

    @pytest.fixture
    def store_with_cert(self):
        store = ACMStore()
        req_handler = _load_handler("request-certificate")
        resp = req_handler(store, {"DomainName": "example.com"})
        return store, resp["CertificateArn"]

    def test_add_tags_happy(self, store_with_cert):
        store, arn = store_with_cert
        handler = _load_handler("add-tags-to-certificate")
        handler(store, {"CertificateArn": arn, "Tags": [
            {"Key": "env", "Value": "prod"},
            {"Key": "team", "Value": "platform"},
        ]})
        list_handler = _load_handler("list-tags-for-certificate")
        result = list_handler(store, {"CertificateArn": arn})
        assert len(result["Tags"]) == 2

    def test_list_tags_not_found(self, store_with_cert):
        store, _ = store_with_cert
        handler = _load_handler("list-tags-for-certificate")
        with pytest.raises(ResourceNotFoundException):
            handler(store, {"CertificateArn": "arn:nonexistent"})

    def test_remove_tags_happy(self, store_with_cert):
        store, arn = store_with_cert
        add_handler = _load_handler("add-tags-to-certificate")
        add_handler(store, {"CertificateArn": arn, "Tags": [
            {"Key": "env", "Value": "prod"},
            {"Key": "team", "Value": "platform"},
        ]})
        rm_handler = _load_handler("remove-tags-from-certificate")
        rm_handler(store, {"CertificateArn": arn, "Tags": [{"Key": "env", "Value": "prod"}]})
        list_handler = _load_handler("list-tags-for-certificate")
        result = list_handler(store, {"CertificateArn": arn})
        assert len(result["Tags"]) == 1
        assert result["Tags"][0]["Key"] == "team"


class TestACMLifecycle:
    """Renew, revoke, update options."""

    @pytest.fixture
    def store_with_cert(self):
        store = ACMStore()
        # Import a cert so it's ISSUED/IMPORTED
        imp_handler = _load_handler("import-certificate")
        resp = imp_handler(store, {
            "Certificate": "test-cert",
            "PrivateKey": "test-key",
        })
        return store, resp["CertificateArn"]

    def test_renew_certificate_not_issued(self, store_with_cert):
        store, _ = store_with_cert
        # Request a cert (PENDING_VALIDATION)
        req_handler = _load_handler("request-certificate")
        resp = req_handler(store, {"DomainName": "example.com"})
        arn = resp["CertificateArn"]

        renew_handler = _load_handler("renew-certificate")
        with pytest.raises(InvalidStateException):
            renew_handler(store, {"CertificateArn": arn})

    def test_revoke_certificate_happy(self, store_with_cert):
        store, arn = store_with_cert
        handler = _load_handler("revoke-certificate")
        handler(store, {"CertificateArn": arn, "RevocationReason": "UNSPECIFIED"})
        desc_handler = _load_handler("describe-certificate")
        result = desc_handler(store, {"CertificateArn": arn})
        assert result["Certificate"]["Status"] == "REVOKED"

    def test_update_options_happy(self, store_with_cert):
        store, arn = store_with_cert
        handler = _load_handler("update-certificate-options")
        handler(store, {"CertificateArn": arn, "Options": {
            "CertificateTransparencyLoggingPreference": "ENABLED",
        }})
        desc_handler = _load_handler("describe-certificate")
        result = desc_handler(store, {"CertificateArn": arn})
        assert result["Certificate"]["Options"]["CertificateTransparencyLoggingPreference"] == "ENABLED"


class TestACMAccountConfig:
    """Get/put account configuration."""

    @pytest.fixture
    def store(self):
        return ACMStore()

    def test_get_account_config_default(self, store):
        handler = _load_handler("get-account-configuration")
        result = handler(store, {})
        assert "ExpiryEvents" in result
        assert "OptInRegions" in result

    def test_put_account_config_happy(self, store):
        put_handler = _load_handler("put-account-configuration")
        put_handler(store, {
            "ExpiryEvents": {"DaysBeforeExpiry": 30},
            "OptInRegions": ["us-east-1"],
        })
        get_handler = _load_handler("get-account-configuration")
        result = get_handler(store, {})
        assert result["ExpiryEvents"]["DaysBeforeExpiry"] == 30
        assert "us-east-1" in result["OptInRegions"]


class TestACMValidation:
    """Resend validation email."""

    @pytest.fixture
    def store(self):
        return ACMStore()

    def test_resend_validation_happy(self, store):
        req_handler = _load_handler("request-certificate")
        resp = req_handler(store, {"DomainName": "example.com"})
        arn = resp["CertificateArn"]

        val_handler = _load_handler("resend-validation-email")
        val_handler(store, {
            "CertificateArn": arn,
            "Domain": "example.com",
            "ValidationDomain": "example.com",
        })

    def test_resend_validation_not_found(self, store):
        handler = _load_handler("resend-validation-email")
        with pytest.raises(ResourceNotFoundException):
            handler(store, {
                "CertificateArn": "arn:nonexistent",
                "Domain": "example.com",
                "ValidationDomain": "example.com",
            })
