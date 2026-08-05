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

# Real self-signed RSA-2048 PEM pair (spec plan: ImportCertificate validates
# PEM, key/cert match, and validity dates — garbage must raise ValidationException).
TEST_CERT_PEM = """-----BEGIN CERTIFICATE-----
MIIDFDCCAfygAwIBAgIUafUK+atVaQLi6n4Nh9MqrT38beIwDQYJKoZIhvcNAQEL
BQAwNjELMAkGA1UEBhMCVVMxETAPBgNVBAoMCFRlc3QgT3JnMRQwEgYDVQQDDAtl
eGFtcGxlLmNvbTAeFw0yNjA4MDQwMDQ5MTVaFw0yNzA4MDUwMDQ5MTVaMDYxCzAJ
BgNVBAYTAlVTMREwDwYDVQQKDAhUZXN0IE9yZzEUMBIGA1UEAwwLZXhhbXBsZS5j
b20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCxvAP2rpz8IhSKwM23
l4LKv9aLEZd++P3z7Br1H91h8uGIApBKsE3LCoLuOOsovjprkDHVBs5xCHwrCWr4
Fp/CpGoF5Kz7NCR3edw3m8I3wdHOV52RGA7gCrVVfsJAAMRCB/rRKmCl/3U+UCHv
QUNBalssjghdK1ZlDSbMCBJZiAF8WdBKfCRYhp0ut9HZgbT6ZQDwo439iQlqx798
o8rHgzuZ9illBHVSHSMOxciUeypy0E8C4gzq52zcHgtd1hUGpvuldin26IHQFYyM
rlQG/HsKAu0yUCY1rT5igN9Nz9M2Ajh1paZ1E446/yUNhIFnzneA7AE94o8JaISK
FanLAgMBAAGjGjAYMBYGA1UdEQQPMA2CC2V4YW1wbGUuY29tMA0GCSqGSIb3DQEB
CwUAA4IBAQCNgu7PSJC8S5kWIuuxm2T4ZR2/xMjppwsIX3YcfcVcV685d0zMEEox
Hy3zEbQbpr77txY+VrgAZ47NAATUCS/adfsE429QrtPzyVF8lsocV0+5XQzeOPxg
kCxLCp5/mNk6P56+L8Nik4sSQCO0WmqFXKhthQh7sQdYz9vSJGJgBwCRRoHe82CT
yO7g8bWGYvsWL8sZNqAdvQCibPxEVIc1hU1shaeA1LRnJR50aKRKPxD88Mi3Pqvo
tLX+LkJe431S+NXqchmRnaT9urW1YO05RuRNfTLFJWeDXoUIva5x6YEVGTNn0rzJ
aWj0NjW++1RvHqbkr3fFUUfERKsehcXH
-----END CERTIFICATE-----
"""
TEST_KEY_PEM = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAsbwD9q6c/CIUisDNt5eCyr/WixGXfvj98+wa9R/dYfLhiAKQ
SrBNywqC7jjrKL46a5Ax1QbOcQh8Kwlq+BafwqRqBeSs+zQkd3ncN5vCN8HRzled
kRgO4Aq1VX7CQADEQgf60Spgpf91PlAh70FDQWpbLI4IXStWZQ0mzAgSWYgBfFnQ
SnwkWIadLrfR2YG0+mUA8KON/YkJase/fKPKx4M7mfYpZQR1Uh0jDsXIlHsqctBP
AuIM6uds3B4LXdYVBqb7pXYp9uiB0BWMjK5UBvx7CgLtMlAmNa0+YoDfTc/TNgI4
daWmdROOOv8lDYSBZ853gOwBPeKPCWiEihWpywIDAQABAoIBABILDsdJDw8k8eXr
eyw4ruKgsAnlNXaCljFgQOpX8PRjy6kwQsVk+Y4ebo/66kX0GIqD6ciBDOMlDonw
m6c85hIZ+S4eUBXzw1dNC+H/UiuxOviSJMuuirq24OrMLVyBrMAxVDFOITVTkOuh
se2P4raDiBGmsksBvnRlbeYHqb6PPWqmsvw6Y7QFlNa6i/iW/cwqlpux56OgloVV
eVvm9jZIFV6oFtpN63EqE/0/vkmlHKKE0BC+2yZ9MPb9MqRVo6yY89M9Q0A1pLfF
0WJpYynu/5vWGFuLRR64b8OKRF8PBW7T68UtDxaw4ze5oysIL7K1gTCtIi7zSDct
N2u5hE0CgYEA+UN0b1+ylEpu3DMc0cCPxMPZjuvjOxhaYNGVPeCPM2EsFEiGrGbF
x6iZdZuVyz2GuUnIC+HTXYAk7ThQEY1uPZhmN7hWfp3K5I59XEGay97WokGIEqr6
gijLy3BKyqIMZu0ynXhmhorTon7r3UrbvOnesR/xeBmc+ZtvFIdFkM8CgYEAtomu
rvJdrFvloqMxrBamkiKIv26AO342iNGUmStae24GT+PnPNKONYsvw50MhJmqpl0i
JfD+u9UFyrWybVEv0uGUSoIbWOxN3/K2oALwYR8Xxmw1WuRc4ZVSONN96n/bmAbb
6H4sZR1HW2SsANbNN230PgM1VdqTOcvHnH5kvkUCgYEA5iyaCnaOS01ojcJNLIvq
tsI71jSRQnK8koc2j0scMU/cCmbmpbDJlhNkkiu36VPJYrR1HDPOoJrCfqPvnCXD
1PE0AuQgSw+e2euSa2zRas092ds1sjdc2HCfsB7jkbaOSUVj5fHWiwsLXxRg7ZpA
y3QTBfD/Y+4S/JPBwW0gmhUCgYB+NiCkMkx2mmvi0jfMJzUxIdOvmTXs7M3EODUo
2wMLCP4wSwJd2bAecYirFnHLVXza3tZ3qXRYZ2hDyvH+B/6rLvIbum4yQ+FskSOY
669NV/RWbAdQO0nFaDubsxADDjjFmyh+To9fsqjeFnOfeOYYB1yzbAB6xlC5y57P
I82AiQKBgQCuXbllNhMBNIX60n3wdQgNKb5yctBerAFneCXt5YHzr5WbWORAjquD
jHj10oC+JiChHTfZ1pGSSmfYJ4aEujs06WOBp9tdko1NmJ1X+FStUsmjiksim7zr
zpihgy+a8gthxCnkCvpjhgfsIJSxBbOqEGUs3R/r8gRkOlDOQ7MopA==
-----END RSA PRIVATE KEY-----
"""


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
            "Certificate": TEST_CERT_PEM,
            "PrivateKey": TEST_KEY_PEM,
        })
        assert "CertificateArn" in resp
        arn = resp["CertificateArn"]
        # Verify it's in the store
        desc_handler = _load_handler("describe-certificate")
        result = desc_handler(store, {"CertificateArn": arn})
        assert result["Certificate"]["Status"] == "ISSUED"

    def test_import_certificate_invalid_pem(self, store):
        handler = _load_handler("import-certificate")
        with pytest.raises(ValidationException):
            handler(store, {
                "Certificate": "-----BEGIN CERTIFICATE-----\ntest\n-----END CERTIFICATE-----",
                "PrivateKey": "-----BEGIN PRIVATE KEY-----\ntest\n-----END PRIVATE KEY-----",
            })
        with pytest.raises(ValidationException):
            handler(store, {"Certificate": "CERT123", "PrivateKey": "KEY123"})

    def test_export_certificate_not_private(self, store):
        imp_handler = _load_handler("import-certificate")
        resp = imp_handler(store, {
            "Certificate": TEST_CERT_PEM,
            "PrivateKey": TEST_KEY_PEM,
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
            "Certificate": TEST_CERT_PEM,
            "PrivateKey": TEST_KEY_PEM,
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
