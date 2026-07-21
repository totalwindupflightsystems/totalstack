"""ACM (AWS Certificate Manager) — Store, records, exceptions."""

import uuid
import time


class ACMException(Exception):
    """Base ACM exception."""
    pass


class InvalidArnException(ACMException):
    pass


class InvalidDomainValidationOptionsException(ACMException):
    pass


class InvalidParameterException(ACMException):
    pass


class InvalidStateException(ACMException):
    pass


class InvalidTagException(ACMException):
    pass


class LimitExceededException(ACMException):
    pass


class RequestInProgressException(ACMException):
    pass


class ResourceInUseException(ACMException):
    pass


class ResourceNotFoundException(ACMException):
    pass


class TooManyTagsException(ACMException):
    pass


class ValidationException(ACMException):
    pass


class CertificateRecord:
    def __init__(self, CertificateArn=None, DomainName="", SubjectAlternativeNames=None,
                 Status="", Type="", KeyAlgorithm="", SignatureAlgorithm="",
                 CreatedAt=None, IssuedAt=None, NotBefore=None, NotAfter=None,
                 RevokedAt=None, RevocationReason="", InUseBy=None,
                 DomainValidationOptions=None, ExtendedKeyUsages=None,
                 RenewalSummary=None, Options=None, Tags=None,
                 CertificateChain=None, Certificate=None, PrivateKey=None,
                 FailureReason=""):
        self.CertificateArn = CertificateArn or f"arn:aws:acm:us-east-1:000000000000:certificate/{uuid.uuid4().hex[:16]}"
        self.DomainName = DomainName
        self.SubjectAlternativeNames = SubjectAlternativeNames or []
        self.Status = Status or "PENDING_VALIDATION"
        self.Type = Type or "AMAZON_ISSUED"
        self.KeyAlgorithm = KeyAlgorithm
        self.SignatureAlgorithm = SignatureAlgorithm
        self.CreatedAt = CreatedAt or time.time()
        self.IssuedAt = IssuedAt
        self.NotBefore = NotBefore
        self.NotAfter = NotAfter
        self.RevokedAt = RevokedAt
        self.RevocationReason = RevocationReason
        self.InUseBy = InUseBy or []
        self.DomainValidationOptions = DomainValidationOptions or []
        self.ExtendedKeyUsages = ExtendedKeyUsages
        self.RenewalSummary = RenewalSummary
        self.Options = Options or {}
        self.Tags = Tags or []
        self.CertificateChain = CertificateChain
        self.Certificate = Certificate
        self.PrivateKey = PrivateKey
        self.FailureReason = FailureReason

    def to_dict(self):
        result = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        # Strip sensitive fields for DescribeCertificate
        result.pop("Certificate", None)
        result.pop("PrivateKey", None)
        result.pop("CertificateChain", None)
        result.pop("Tags", None)
        # Add computed fields AWS expects
        result.setdefault("Issuer", "Amazon")
        result.setdefault("Subject", f"CN={self.DomainName}")
        result.setdefault("Serial", "")
        result.setdefault("KeyUsages", [{"Name": "DIGITAL_SIGNATURE"}, {"Name": "KEY_ENCIPHERMENT"}])
        result.setdefault("RenewalEligibility", "INELIGIBLE")
        # Strip optional enum fields when empty — AWS omits them entirely
        for field in ("RevocationReason", "FailureReason", "ManagedBy", "KeyAlgorithm"):
            if result.get(field) == "":
                result.pop(field, None)
        return result


class ACMStore:
    def __init__(self):
        self._certificates: dict[str, CertificateRecord] = {}
        self._account_config = {"ExpiryEvents": {}, "OptInRegions": []}
        self._max_certificates = 1000

    def certificates(self, arn: str = None):
        if arn is not None:
            return self._certificates.get(arn)
        return [c.to_dict() for c in self._certificates.values()]

    # --- Certificate CRUD ---

    def request_certificate(self, DomainName: str, SubjectAlternativeNames: list = None,
                            ValidationMethod: str = "EMAIL", Options: dict = None,
                            IdempotencyToken: str = None,
                            CertificateAuthorityArn: str = None, Tags: list = None,
                            KeyAlgorithm: str = "RSA_2048") -> dict:
        if len(self._certificates) >= self._max_certificates:
            raise LimitExceededException("Certificate limit exceeded")
        record = CertificateRecord(
            DomainName=DomainName,
            SubjectAlternativeNames=SubjectAlternativeNames or [],
            Status="PENDING_VALIDATION",
            Type="AMAZON_ISSUED",
            KeyAlgorithm=KeyAlgorithm,
            DomainValidationOptions=[],
            Options=Options or {},
            Tags=Tags or [],
        )
        self._certificates[record.CertificateArn] = record
        return {"CertificateArn": record.CertificateArn}

    def import_certificate(self, Certificate: str, PrivateKey: str,
                           CertificateChain: str = None, CertificateArn: str = None,
                           Tags: list = None) -> dict:
        arn = CertificateArn or f"arn:aws:acm:us-east-1:000000000000:certificate/{uuid.uuid4().hex[:16]}"
        record = CertificateRecord(
            CertificateArn=arn,
            Status="IMPORTED",
            Type="IMPORTED",
            Certificate=Certificate,
            PrivateKey=PrivateKey,
            CertificateChain=CertificateChain or "",
            Tags=Tags or [],
        )
        self._certificates[arn] = record
        return {"CertificateArn": arn}

    def describe_certificate(self, CertificateArn: str) -> dict:
        record = self._certificates.get(CertificateArn)
        if not record:
            raise ResourceNotFoundException(f"Certificate {CertificateArn} not found")
        result = record.to_dict()
        result.pop("Certificate", None)
        result.pop("PrivateKey", None)
        return {"Certificate": result}

    def get_certificate(self, CertificateArn: str) -> dict:
        record = self._certificates.get(CertificateArn)
        if not record:
            raise ResourceNotFoundException(f"Certificate {CertificateArn} not found")
        if record.Status != "ISSUED":
            raise InvalidStateException("Certificate not yet issued")
        return {
            "Certificate": record.Certificate or "",
            "CertificateChain": record.CertificateChain or "",
            "PrivateKey": record.PrivateKey or "",
        }

    def list_certificates(self, CertificateStatuses: list = None,
                          Includes: dict = None, NextToken: str = None,
                          MaxItems: int = 50) -> dict:
        certs = list(self._certificates.values())
        if CertificateStatuses:
            certs = [c for c in certs if c.Status in CertificateStatuses]
        return {"CertificateSummaryList": [{
            "CertificateArn": c.CertificateArn,
            "DomainName": c.DomainName,
            "SubjectAlternativeNameSummaries": c.SubjectAlternativeNames or [],
            "Status": c.Status,
            "Type": c.Type,
            "KeyAlgorithm": c.KeyAlgorithm,
            "InUse": bool(c.InUseBy),
            "HasAdditionalSubjectAlternativeNames": len(c.SubjectAlternativeNames or []) > 1,
            "CreatedAt": c.CreatedAt,
            "ImportedAt": c.CreatedAt if c.Type == "IMPORTED" else None,
        } for c in certs[:MaxItems]], "NextToken": None}

    def delete_certificate(self, CertificateArn: str) -> dict:
        record = self._certificates.get(CertificateArn)
        if not record:
            raise ResourceNotFoundException(f"Certificate {CertificateArn} not found")
        if record.InUseBy:
            raise ResourceInUseException("Certificate is in use")
        del self._certificates[CertificateArn]
        return {}

    def export_certificate(self, CertificateArn: str, Passphrase: bytes) -> dict:
        record = self._certificates.get(CertificateArn)
        if not record:
            raise ResourceNotFoundException(f"Certificate {CertificateArn} not found")
        if record.Type != "PRIVATE":
            raise InvalidStateException("Only private certificates can be exported")
        return {
            "Certificate": record.Certificate or "",
            "CertificateChain": record.CertificateChain or "",
            "PrivateKey": record.PrivateKey or "",
        }

    # --- Lifecycle ---

    def renew_certificate(self, CertificateArn: str) -> dict:
        record = self._certificates.get(CertificateArn)
        if not record:
            raise ResourceNotFoundException(f"Certificate {CertificateArn} not found")
        if record.Status != "ISSUED":
            raise InvalidStateException("Certificate not in ISSUED state")
        record.Status = "PENDING_VALIDATION"
        record.RenewalSummary = {"RenewalStatus": "PENDING_VALIDATION", "DomainValidationOptions": []}
        return {}

    def revoke_certificate(self, CertificateArn: str, RevocationReason: str) -> dict:
        record = self._certificates.get(CertificateArn)
        if not record:
            raise ResourceNotFoundException(f"Certificate {CertificateArn} not found")
        record.Status = "REVOKED"
        record.RevokedAt = time.time()
        record.RevocationReason = RevocationReason
        return {}

    def update_certificate_options(self, CertificateArn: str, Options: dict) -> dict:
        record = self._certificates.get(CertificateArn)
        if not record:
            raise ResourceNotFoundException(f"Certificate {CertificateArn} not found")
        record.Options = Options
        return {}

    # --- Tags ---

    def add_tags_to_certificate(self, CertificateArn: str, Tags: list) -> dict:
        record = self._certificates.get(CertificateArn)
        if not record:
            raise ResourceNotFoundException(f"Certificate {CertificateArn} not found")
        if len(record.Tags) + len(Tags) > 50:
            raise TooManyTagsException("Tag limit exceeded")
        for tag in Tags:
            for k, v in tag.items():
                if len(str(k)) > 128 or len(str(v)) > 256:
                    raise InvalidTagException("Tag key or value too long")
        record.Tags.extend(Tags)
        return {}

    def list_tags_for_certificate(self, CertificateArn: str) -> dict:
        record = self._certificates.get(CertificateArn)
        if not record:
            raise ResourceNotFoundException(f"Certificate {CertificateArn} not found")
        return {"Tags": record.Tags}

    def remove_tags_from_certificate(self, CertificateArn: str, Tags: list) -> dict:
        record = self._certificates.get(CertificateArn)
        if not record:
            raise ResourceNotFoundException(f"Certificate {CertificateArn} not found")
        for tag in Tags:
            record.Tags = [t for t in record.Tags if t.get("Key") != tag.get("Key")]
        return {}

    # --- Account config ---

    def get_account_configuration(self) -> dict:
        return dict(self._account_config)

    def put_account_configuration(self, ExpiryEvents: dict = None,
                                  IdempotencyToken: str = None,
                                  OptInRegions: list = None) -> dict:
        if ExpiryEvents is not None:
            self._account_config["ExpiryEvents"] = ExpiryEvents
        if OptInRegions is not None:
            self._account_config["OptInRegions"] = OptInRegions
        return {}

    # --- Validation ---

    def resend_validation_email(self, CertificateArn: str, Domain: str,
                                ValidationDomain: str) -> dict:
        record = self._certificates.get(CertificateArn)
        if not record:
            raise ResourceNotFoundException(f"Certificate {CertificateArn} not found")
        if record.Status != "PENDING_VALIDATION":
            raise InvalidStateException("Certificate not in PENDING_VALIDATION state")
        return {}
