"""
TotalStack ACM Provider — replaces moto backend with our ACMStore.
Drop-in replacement for localstack.services.acm.provider.AcmProvider.
"""
import importlib.util
import logging
import os

from localstack.aws.api import RequestContext, handler
from localstack.aws.api.acm import (
    AcmApi,
    InvalidParameterException,
    InvalidStateException,
    InvalidTagException,
    LimitExceededException,
    ResourceInUseException,
    ResourceNotFoundException,
    TooManyTagsException,
    ValidationException,
)

LOG = logging.getLogger(__name__)

# Path to our assembled handlers + models
_totalstack_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_svc_path = os.path.join(_totalstack_path, "specs", "aws", ".speclang", "assembled", "acm")

# Mount exception map: our custom exceptions → LocalStack ServiceException subclasses
EXCEPTION_MAP = {
    "InvalidParameterException": InvalidParameterException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceInUseException": ResourceInUseException,
    "InvalidStateException": InvalidStateException,
    "LimitExceededException": LimitExceededException,
    "TooManyTagsException": TooManyTagsException,
    "InvalidTagException": InvalidTagException,
    "ValidationException": ValidationException,
}

# Import store
models_spec = importlib.util.spec_from_file_location(
    "models", os.path.join(_svc_path, "models.code.py"))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)
ACMStore = models_mod.ACMStore


def _reraise_as_service(store_fn):
    """Decorator: catch our custom exceptions, re-raise as LocalStack ServiceException."""
    import functools
    @functools.wraps(store_fn)
    def wrapper(*args, **kwargs):
        try:
            return store_fn(*args, **kwargs)
        except Exception as e:
            name = type(e).__name__
            if name in EXCEPTION_MAP:
                # Re-raise as proper AWS exception with message
                ls_exc = EXCEPTION_MAP[name]
                raise ls_exc(str(e)) from e
            raise
    return wrapper


class TotalStackAcmProvider(AcmApi):
    """ACM provider backed by TotalStack's real ACMStore — no moto."""

    def __init__(self):
        self.store = ACMStore()

    @handler("RequestCertificate", expand=False)
    def request_certificate(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.request_certificate)(
            DomainName=request.get("DomainName", ""),
            SubjectAlternativeNames=request.get("SubjectAlternativeNames"),
            ValidationMethod=request.get("ValidationMethod", "EMAIL"),
            Options=request.get("Options"),
            IdempotencyToken=request.get("IdempotencyToken"),
            CertificateAuthorityArn=request.get("CertificateAuthorityArn"),
            Tags=request.get("Tags"),
            KeyAlgorithm=request.get("KeyAlgorithm", "RSA_2048"),
        )

    @handler("ImportCertificate", expand=False)
    def import_certificate(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.import_certificate)(
            Certificate=request.get("Certificate", ""),
            PrivateKey=request.get("PrivateKey", ""),
            CertificateChain=request.get("CertificateChain"),
            CertificateArn=request.get("CertificateArn"),
            Tags=request.get("Tags"),
        )

    @handler("DescribeCertificate", expand=False)
    def describe_certificate(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.describe_certificate)(
            CertificateArn=request.get("CertificateArn", ""),
        )

    @handler("GetCertificate", expand=False)
    def get_certificate(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.get_certificate)(
            CertificateArn=request.get("CertificateArn", ""),
        )

    @handler("ListCertificates", expand=False)
    def list_certificates(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.list_certificates)(
            CertificateStatuses=request.get("CertificateStatuses"),
            Includes=request.get("Includes"),
            NextToken=request.get("NextToken"),
            MaxItems=request.get("MaxItems", 50),
        )

    @handler("DeleteCertificate", expand=False)
    def delete_certificate(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.delete_certificate)(
            CertificateArn=request.get("CertificateArn", ""),
        )

    @handler("ExportCertificate", expand=False)
    def export_certificate(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.export_certificate)(
            CertificateArn=request.get("CertificateArn", ""),
            Passphrase=request.get("Passphrase", b""),
        )

    @handler("RenewCertificate", expand=False)
    def renew_certificate(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.renew_certificate)(
            CertificateArn=request.get("CertificateArn", ""),
        )

    @handler("RevokeCertificate", expand=False)
    def revoke_certificate(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.revoke_certificate)(
            CertificateArn=request.get("CertificateArn", ""),
            RevocationReason=request.get("RevocationReason", "UNSPECIFIED"),
        )

    @handler("UpdateCertificateOptions", expand=False)
    def update_certificate_options(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.update_certificate_options)(
            CertificateArn=request.get("CertificateArn", ""),
            Options=request.get("Options", {}),
        )

    @handler("AddTagsToCertificate", expand=False)
    def add_tags_to_certificate(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.add_tags_to_certificate)(
            CertificateArn=request.get("CertificateArn", ""),
            Tags=request.get("Tags", []),
        )

    @handler("ListTagsForCertificate", expand=False)
    def list_tags_for_certificate(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.list_tags_for_certificate)(
            CertificateArn=request.get("CertificateArn", ""),
        )

    @handler("RemoveTagsFromCertificate", expand=False)
    def remove_tags_from_certificate(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.remove_tags_from_certificate)(
            CertificateArn=request.get("CertificateArn", ""),
            Tags=request.get("Tags", []),
        )

    @handler("GetAccountConfiguration", expand=False)
    def get_account_configuration(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.get_account_configuration)()

    @handler("PutAccountConfiguration", expand=False)
    def put_account_configuration(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.put_account_configuration)(
            ExpiryEvents=request.get("ExpiryEvents"),
            IdempotencyToken=request.get("IdempotencyToken"),
            OptInRegions=request.get("OptInRegions"),
        )

    @handler("ResendValidationEmail", expand=False)
    def resend_validation_email(self, context: RequestContext, request: dict) -> dict:
        return _reraise_as_service(self.store.resend_validation_email)(
            CertificateArn=request.get("CertificateArn", ""),
            Domain=request.get("Domain", ""),
            ValidationDomain=request.get("ValidationDomain", ""),
        )
