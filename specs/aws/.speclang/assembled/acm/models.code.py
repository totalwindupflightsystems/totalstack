"""ACM (AWS Certificate Manager) — Store, records, exceptions."""

import hashlib
import re
import time
import uuid

from moto import settings as moto_settings

from cryptography import x509 as crypto_x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec, rsa
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.x509.oid import ExtensionOID, NameOID

# Reduce the validation wait time from 60 (moto default) to 10 seconds, the same
# behavior LocalStack's own ACM provider applies at import time. Tests that rely
# on auto-issuance monkeypatch moto_settings.ACM_VALIDATION_WAIT per test; the
# lazy transition in CertificateRecord.check() reads it dynamically.
moto_settings.ACM_VALIDATION_WAIT = min(10, moto_settings.ACM_VALIDATION_WAIT)


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


# cryptography key-usage attribute -> AWS KeyUsage Name
_KEY_USAGE_NAMES = {
    "digital_signature": "DIGITAL_SIGNATURE",
    "non_repudiation": "NON_REPUDIATION",
    "key_encipherment": "KEY_ENCIPHERMENT",
    "data_encipherment": "DATA_ENCIPHERMENT",
    "key_agreement": "KEY_AGREEMENT",
    "key_cert_sign": "KEY_CERT_SIGN",
    "crl_sign": "CRL_SIGN",
    "encipher_only": "ENCIPHER_ONLY",
    "decipher_only": "DECIPHER_ONLY",
}

# extended-key-usage OID -> AWS ExtendedKeyUsage Name
_EKU_NAME_BY_OID = {
    "1.3.6.1.5.5.7.3.1": "TLS_WEB_SERVER_AUTHENTICATION",
    "1.3.6.1.5.5.7.3.2": "TLS_WEB_CLIENT_AUTHENTICATION",
    "1.3.6.1.5.5.7.3.3": "CODE_SIGNING",
    "1.3.6.1.5.5.7.3.4": "EMAIL_PROTECTION",
    "1.3.6.1.5.5.7.3.8": "TIME_STAMPING",
    "1.3.6.1.5.5.7.3.9": "OCSP_SIGNING",
}

_CURVE_NAME_MAP = {
    "secp256r1": "prime256v1",
    "secp384r1": "secp384r1",
    "secp521r1": "secp521r1",
}

_TWO_YEARS = 2 * 365 * 24 * 60 * 60


def _as_bytes(value):
    """Coerce blob values (bytes or str) to bytes for PEM parsing."""
    return value if isinstance(value, bytes) else str(value).encode("utf-8")


def _load_certificate(cert_bytes):
    try:
        return crypto_x509.load_pem_x509_certificate(cert_bytes)
    except Exception:
        raise ValidationException("The certificate is not PEM-encoded or is not valid.")


def _load_private_key(key_bytes):
    try:
        return serialization.load_pem_private_key(key_bytes, password=None)
    except Exception:
        raise ValidationException("The private key is not PEM-encoded or is not valid.")


def _validate_key_matches(cert, key):
    """AWS rejects imports where the private key does not match the certificate."""
    try:
        cert_public = cert.public_key().public_bytes(
            Encoding.DER, PublicFormat.SubjectPublicKeyInfo
        )
        key_public = key.public_key().public_bytes(
            Encoding.DER, PublicFormat.SubjectPublicKeyInfo
        )
    except Exception:
        raise ValidationException("The private key does not match the certificate.")
    if cert_public != key_public:
        raise ValidationException("The private key does not match the certificate.")


def _cert_not_valid_before(cert):
    try:
        return cert.not_valid_before_utc
    except AttributeError:
        return cert.not_valid_before


def _cert_not_valid_after(cert):
    try:
        return cert.not_valid_after_utc
    except AttributeError:
        return cert.not_valid_after


def _validate_cert_dates(cert):
    now = time.time()
    if _cert_not_valid_before(cert).timestamp() > now:
        raise ValidationException("The certificate is not in effect yet, is not valid.")
    if _cert_not_valid_after(cert).timestamp() < now:
        raise ValidationException("The certificate has expired, is not valid.")


def _validate_chain(chain_bytes):
    try:
        pems = re.findall(
            rb"-----BEGIN CERTIFICATE-----.*?-----END CERTIFICATE-----",
            chain_bytes,
            re.DOTALL,
        )
        for pem in pems:
            crypto_x509.load_pem_x509_certificate(pem)
    except Exception:
        raise ValidationException("The certificate chain is not PEM-encoded or is not valid.")


def _parse_certificate_metadata(cert, key):
    """Extract AWS-facing fields from an imported certificate + private key."""
    domain_name = ""
    try:
        cn = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
        domain_name = cn[0].value if cn else ""
    except Exception:
        pass

    sans = []
    try:
        san_ext = cert.extensions.get_extension_for_oid(
            ExtensionOID.SUBJECT_ALTERNATIVE_NAME
        )
        sans = [str(item.value) for item in san_ext.value]
    except Exception:
        pass
    if domain_name and domain_name not in sans:
        sans.insert(0, domain_name)

    if isinstance(key, rsa.RSAPrivateKey):
        key_algorithm = f"RSA_{key.key_size}"
    elif isinstance(key, ec.EllipticCurvePrivateKey):
        curve_name = key.curve.name.lower()
        aws_curve = _CURVE_NAME_MAP.get(curve_name, curve_name)
        key_algorithm = f"EC_{aws_curve}"
    else:
        key_algorithm = "RSA_2048"

    signature_algorithm = cert.signature_algorithm_oid._name.upper().replace(
        "ENCRYPTION", ""
    )

    key_usages = []
    try:
        ku = cert.extensions.get_extension_for_oid(ExtensionOID.KEY_USAGE).value
        for attr, name in _KEY_USAGE_NAMES.items():
            if getattr(ku, attr, False):
                key_usages.append(name)
    except Exception:
        pass

    extended_key_usages = []
    try:
        eku = cert.extensions.get_extension_for_oid(
            ExtensionOID.EXTENDED_KEY_USAGE
        ).value
        for oid in eku:
            name = _EKU_NAME_BY_OID.get(oid.dotted_string)
            if name:
                extended_key_usages.append({"Name": name, "OID": oid.dotted_string})
    except Exception:
        pass

    issuer = ""
    try:
        iss = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)
        issuer = iss[0].value if iss else ""
    except Exception:
        pass

    return {
        "domain_name": domain_name,
        "sans": sans,
        "key_algorithm": key_algorithm,
        "signature_algorithm": signature_algorithm,
        "not_before": _cert_not_valid_before(cert).timestamp(),
        "not_after": _cert_not_valid_after(cert).timestamp(),
        "serial": str(cert.serial_number),
        "issuer": issuer,
        "key_usages": key_usages,
        "extended_key_usages": extended_key_usages,
    }


class CertificateRecord:
    def __init__(self, CertificateArn=None, DomainName="", SubjectAlternativeNames=None,
                 Status="", Type="", KeyAlgorithm="", SignatureAlgorithm="",
                 CreatedAt=None, IssuedAt=None, NotBefore=None, NotAfter=None,
                 RevokedAt=None, RevocationReason="", InUseBy=None,
                 DomainValidationOptions=None, ExtendedKeyUsages=None,
                 RenewalSummary=None, Options=None, Tags=None,
                 CertificateChain=None, Certificate=None, PrivateKey=None,
                 FailureReason="", ValidationMethod=None, ImportedAt=None,
                 Issuer=None, Serial=None, KeyUsages=None):
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
        self.ExtendedKeyUsages = ExtendedKeyUsages or []
        self.RenewalSummary = RenewalSummary
        self.Options = Options or {}
        self.Tags = Tags or []
        self.CertificateChain = CertificateChain
        self.Certificate = Certificate
        self.PrivateKey = PrivateKey
        self.FailureReason = FailureReason
        self.ValidationMethod = ValidationMethod
        self.ImportedAt = ImportedAt
        self.Issuer = Issuer
        self.Serial = Serial
        self.KeyUsages = KeyUsages or []

    def check(self):
        """Lazy auto-issuance: flip PENDING_VALIDATION -> ISSUED once the moto
        ACM_VALIDATION_WAIT window (seconds) has elapsed since creation. Mirrors
        moto's CertBundle.check() so waiters and describe/list/get polls observe
        issuance without a background thread."""
        if self.Type == "AMAZON_ISSUED" and self.Status == "PENDING_VALIDATION":
            waited = time.time() - self.CreatedAt
            if waited >= moto_settings.ACM_VALIDATION_WAIT:
                self.Status = "ISSUED"
                self.IssuedAt = time.time()
                self.NotBefore = self.NotBefore or self.CreatedAt
                self.NotAfter = self.NotAfter or (self.CreatedAt + _TWO_YEARS)
                self.Serial = self.Serial or uuid.uuid4().hex[:8]

    # --- field helpers ---

    def _all_domains(self):
        """DomainName plus every SAN, deduplicated, DomainName first."""
        domains = list(self.SubjectAlternativeNames or [])
        if self.DomainName and self.DomainName not in domains:
            domains.insert(0, self.DomainName)
        return domains

    def _normalized_key_algorithm(self):
        """AWS returns KeyAlgorithm with hyphens (RSA-2048) in responses while
        the request enum uses underscores (RSA_2048)."""
        alg = self.KeyAlgorithm or "RSA_2048"
        if alg.startswith("RSA_"):
            return f"RSA-{alg[4:]}"
        if alg.startswith("EC_"):
            return f"EC-{alg[3:]}"
        return alg

    def _validation_status(self):
        return "SUCCESS" if self.Status == "ISSUED" else "PENDING_VALIDATION"

    def _domain_validation_options(self):
        status = self._validation_status()
        method = self.ValidationMethod or "EMAIL"
        options = []
        for domain in self._all_domains():
            option = {
                "DomainName": domain,
                "ValidationDomain": domain,
                "ValidationStatus": status,
                "ValidationMethod": method,
            }
            if method == "DNS":
                digest = hashlib.md5(domain.encode("utf-8")).hexdigest()
                record_domain = domain[2:] if domain.startswith("*.") else domain
                option["ResourceRecord"] = {
                    "Name": f"_{digest}.{record_domain}.",
                    "Type": "CNAME",
                    "Value": f"{digest}.acm-validations.aws.",
                }
            else:
                option["ValidationEmails"] = []
            options.append(option)
        return options

    def describe_key_usages(self):
        if self.Type == "IMPORTED":
            return [{"Name": name} for name in self.KeyUsages]
        if self.Status == "ISSUED":
            return [{"Name": "DIGITAL_SIGNATURE"}, {"Name": "KEY_ENCIPHERMENT"}]
        return []

    def describe_extended_key_usages(self):
        if self.Type == "IMPORTED":
            return list(self.ExtendedKeyUsages)
        if self.Status == "ISSUED":
            return [
                {"Name": "TLS_WEB_SERVER_AUTHENTICATION", "OID": "1.3.6.1.0.1.2.3.0"},
                {"Name": "TLS_WEB_CLIENT_AUTHENTICATION", "OID": "1.3.6.1.0.1.2.3.4"},
            ]
        return []

    def summary_key_usages(self):
        if self.Type == "IMPORTED":
            return list(self.KeyUsages)
        if self.Status == "ISSUED":
            return ["DIGITAL_SIGNATURE", "KEY_ENCIPHERMENT"]
        return []

    def summary_extended_key_usages(self):
        if self.Type == "IMPORTED":
            return [e["Name"] for e in self.ExtendedKeyUsages]
        if self.Status == "ISSUED":
            return ["TLS_WEB_SERVER_AUTHENTICATION", "TLS_WEB_CLIENT_AUTHENTICATION"]
        return []

    def to_dict(self):
        """DescribeCertificate payload. Sensitive fields (Certificate,
        PrivateKey, CertificateChain, Tags) are stripped by the store."""
        result = {
            "CertificateArn": self.CertificateArn,
            "CreatedAt": self.CreatedAt,
            "DomainName": self.DomainName,
            "InUseBy": self.InUseBy or [],
            "Issuer": self.Issuer or "Amazon",
            "KeyAlgorithm": self._normalized_key_algorithm(),
            "Options": self.Options or {},
            "RenewalEligibility": "INELIGIBLE",
            "SignatureAlgorithm": self.SignatureAlgorithm or "SHA256WITHRSA",
            "Status": self.Status,
            "Subject": f"CN={self.DomainName}",
            "SubjectAlternativeNames": self.SubjectAlternativeNames or [],
            "Type": self.Type,
            "KeyUsages": self.describe_key_usages(),
            "ExtendedKeyUsages": self.describe_extended_key_usages(),
        }
        issued = self.Status == "ISSUED"
        if self.Type == "IMPORTED":
            result["ImportedAt"] = self.ImportedAt or self.CreatedAt
            result["DomainValidationOptions"] = [
                {"DomainName": domain} for domain in self._all_domains()
            ]
            if self.NotBefore:
                result["NotBefore"] = self.NotBefore
            if self.NotAfter:
                result["NotAfter"] = self.NotAfter
            if self.Serial:
                result["Serial"] = str(self.Serial)
        else:
            result["DomainValidationOptions"] = self._domain_validation_options()
            if issued:
                result["IssuedAt"] = self.IssuedAt or self.CreatedAt
                result["NotBefore"] = self.NotBefore or self.CreatedAt
                result["NotAfter"] = self.NotAfter or (self.CreatedAt + _TWO_YEARS)
                result["Serial"] = str(self.Serial or "")
        # Strip optional enum fields when empty — AWS omits them entirely
        for field in ("RevocationReason", "FailureReason", "ManagedBy"):
            if not result.get(field):
                result.pop(field, None)
        return result


class ACMStore:
    def __init__(self):
        self._certificates: dict[str, CertificateRecord] = {}
        self._account_config = {"ExpiryEvents": {}, "OptInRegions": []}
        self._max_certificates = 1000

    def certificates(self, arn: str = None):
        if arn is not None:
            record = self._certificates.get(arn)
            if record:
                record.check()
            return record
        for record in self._certificates.values():
            record.check()
        return [c.to_dict() for c in self._certificates.values()]

    def _get_record(self, arn: str) -> CertificateRecord:
        record = self._certificates.get(arn)
        if not record:
            raise ResourceNotFoundException(f"Certificate {arn} not found")
        record.check()
        return record

    # --- Certificate CRUD ---

    def request_certificate(self, DomainName: str, SubjectAlternativeNames: list = None,
                            ValidationMethod: str = "EMAIL", Options: dict = None,
                            IdempotencyToken: str = None,
                            CertificateAuthorityArn: str = None, Tags: list = None,
                            KeyAlgorithm: str = "RSA_2048") -> dict:
        if len(self._certificates) >= self._max_certificates:
            raise LimitExceededException("Certificate limit exceeded")
        sans = list(SubjectAlternativeNames or [])
        if DomainName and DomainName not in sans:
            sans.insert(0, DomainName)
        if Options is None:
            Options = {
                "CertificateTransparencyLoggingPreference": "ENABLED",
                "Export": "DISABLED",
            }
        record = CertificateRecord(
            DomainName=DomainName,
            SubjectAlternativeNames=sans,
            Status="PENDING_VALIDATION",
            Type="AMAZON_ISSUED",
            KeyAlgorithm=KeyAlgorithm or "RSA_2048",
            SignatureAlgorithm="SHA256WITHRSA",
            ValidationMethod=ValidationMethod or "EMAIL",
            Options=Options,
            Tags=Tags or [],
        )
        self._certificates[record.CertificateArn] = record
        return {"CertificateArn": record.CertificateArn}

    def import_certificate(self, Certificate: str, PrivateKey: str,
                           CertificateChain: str = None, CertificateArn: str = None,
                           Tags: list = None) -> dict:
        cert_bytes = _as_bytes(Certificate)
        key_bytes = _as_bytes(PrivateKey)
        cert = _load_certificate(cert_bytes)
        key = _load_private_key(key_bytes)
        _validate_key_matches(cert, key)
        _validate_cert_dates(cert)
        if CertificateChain:
            _validate_chain(_as_bytes(CertificateChain))
        metadata = _parse_certificate_metadata(cert, key)
        arn = CertificateArn or f"arn:aws:acm:us-east-1:000000000000:certificate/{uuid.uuid4().hex[:16]}"
        record = CertificateRecord(
            CertificateArn=arn,
            DomainName=metadata["domain_name"],
            SubjectAlternativeNames=metadata["sans"],
            Status="ISSUED",
            Type="IMPORTED",
            KeyAlgorithm=metadata["key_algorithm"],
            SignatureAlgorithm=metadata["signature_algorithm"],
            NotBefore=metadata["not_before"],
            NotAfter=metadata["not_after"],
            Serial=metadata["serial"],
            Issuer=metadata["issuer"],
            KeyUsages=metadata["key_usages"],
            ExtendedKeyUsages=metadata["extended_key_usages"],
            Options={
                "CertificateTransparencyLoggingPreference": "DISABLED",
                "Export": "DISABLED",
            },
            Certificate=Certificate,
            PrivateKey=PrivateKey,
            CertificateChain=CertificateChain or "",
            Tags=Tags or [],
        )
        self._certificates[arn] = record
        return {"CertificateArn": arn}

    def describe_certificate(self, CertificateArn: str) -> dict:
        record = self._get_record(CertificateArn)
        result = record.to_dict()
        result.pop("Certificate", None)
        result.pop("PrivateKey", None)
        result.pop("CertificateChain", None)
        result.pop("Tags", None)
        return {"Certificate": result}

    def get_certificate(self, CertificateArn: str) -> dict:
        record = self._get_record(CertificateArn)
        if record.Status != "ISSUED":
            raise InvalidStateException("Certificate not yet issued")
        return {
            "Certificate": record.Certificate or "",
            "CertificateChain": record.CertificateChain or "",
            "PrivateKey": record.PrivateKey or "",
        }

    @staticmethod
    def _summary(record: CertificateRecord) -> dict:
        issued = record.Status == "ISSUED"
        summary = {
            "CertificateArn": record.CertificateArn,
            "DomainName": record.DomainName,
            "SubjectAlternativeNameSummaries": record.SubjectAlternativeNames or [],
            "HasAdditionalSubjectAlternativeNames": False,
            "Status": record.Status,
            "Type": record.Type,
            "KeyAlgorithm": record._normalized_key_algorithm(),
            "InUse": bool(record.InUseBy),
            "RenewalEligibility": "INELIGIBLE",
            "CreatedAt": record.CreatedAt,
            "Exported": False,
            "KeyUsages": record.summary_key_usages(),
            "ExtendedKeyUsages": record.summary_extended_key_usages(),
        }
        if issued:
            summary["NotBefore"] = record.NotBefore or record.CreatedAt
            summary["NotAfter"] = record.NotAfter or (record.CreatedAt + _TWO_YEARS)
            if record.Type == "AMAZON_ISSUED":
                summary["IssuedAt"] = record.IssuedAt or record.CreatedAt
        if record.Type == "IMPORTED":
            summary["ImportedAt"] = record.ImportedAt or record.CreatedAt
        return summary

    def list_certificates(self, CertificateStatuses: list = None,
                          Includes: dict = None, NextToken: str = None,
                          MaxItems: int = 50) -> dict:
        certs = list(self._certificates.values())
        for record in certs:
            record.check()
        if CertificateStatuses:
            certs = [c for c in certs if c.Status in CertificateStatuses]
        key_types = (Includes or {}).get("keyTypes")
        if key_types:
            # Request enum format (RSA_2048) matches the stored KeyAlgorithm.
            certs = [c for c in certs if c.KeyAlgorithm in key_types]
        return {"CertificateSummaryList": [self._summary(c) for c in certs[:MaxItems]]}

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
