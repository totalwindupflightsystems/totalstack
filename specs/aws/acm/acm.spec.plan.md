---
id: acm-plan
title: ACM Implementation Plan
target_lang: py
depends_on: ["specs/aws/acm/acm.spec.meta.md"]
---

# ACM Implementation Plan

## Store: ACMStore

Single dict-backed store for certificate records. Key: CertificateArn.

## Store Semantics (AWS parity)

- **ImportCertificate validation** — `import_certificate` raises
  `ValidationException` when the Certificate/PrivateKey are not valid PEM
  (parsed via cryptography `load_pem_x509_certificate` /
  `load_pem_private_key`), when the private key does not match the
  certificate public key, when the certificate is expired or not yet in
  effect, or when the optional CertificateChain contains invalid PEM.
  Imported certs are stored `Status=ISSUED`, `Type=IMPORTED`, with
  DomainName/SANs/KeyAlgorithm/SignatureAlgorithm/validity parsed from the
  certificate itself. Options default to
  `{"CertificateTransparencyLoggingPreference": "DISABLED", "Export": "DISABLED"}`.
- **RequestCertificate validation options** — `request_certificate` stores
  `Status=PENDING_VALIDATION`, `Type=AMAZON_ISSUED`. DNS validation
  (`ValidationMethod="DNS"`) yields DomainValidationOptions entries with a
  CNAME `ResourceRecord` (`Name: _<hash>.<domain>.`, `Value: <hash>.acm-validations.aws.`,
  `Type: CNAME`); EMAIL yields entries with `ValidationEmails: []`. Options
  default to
  `{"CertificateTransparencyLoggingPreference": "ENABLED", "Export": "DISABLED"}`.
- **Auto-issuance** — an AMAZON_ISSUED cert transitions
  PENDING_VALIDATION → ISSUED after `moto_settings.ACM_VALIDATION_WAIT`
  seconds (moto default 60, lowered to 10 at store import; tests
  monkeypatch it to 1–2). The transition is lazy: `check()` runs on
  describe/get/list and flips Status, sets IssuedAt/NotBefore/NotAfter/Serial
  and marks DomainValidationOptions `ValidationStatus=SUCCESS`. Imported
  certs never transition.
- **ListCertificates Includes filter** — `Includes.keyTypes` filters
  summaries on the stored KeyAlgorithm (request enum format, e.g.
  `RSA_2048`). Summary items expose KeyAlgorithm in response format
  (`RSA-2048`), `Exported: false`, KeyUsages/ExtendedKeyUsages as string
  lists (empty while PENDING_VALIDATION), and IssuedAt only for
  AMAZON_ISSUED certs (ImportedAt for imported). `HasAdditionalSubjectAlternativeNames`
  is always false (moto parity).

## Exceptions
- InvalidArnException — malformed ARN
- InvalidDomainValidationOptionsException — bad domain opts
- InvalidParameterException — bad params
- InvalidStateException — wrong state for operation
- InvalidTagException — bad tag format
- LimitExceededException — too many certificates
- RequestInProgressException — duplicate request
- ResourceInUseException — cert in use
- ResourceNotFoundException — cert not found
- TooManyTagsException — tag limit exceeded
- ValidationException — validation error

## CertificateRecord Fields
- CertificateArn, DomainName, SubjectAlternativeNames, Status (PENDING_VALIDATION/ISSUED/INACTIVE/REVOKED/EXPIRED/FAILED/IMPORTED), Type (IMPORTED/AMAZON_ISSUED/PRIVATE), KeyAlgorithm, SignatureAlgorithm, CreatedAt, IssuedAt, NotBefore, NotAfter, RevokedAt, RevocationReason, InUseBy, DomainValidationOptions, ExtendedKeyUsages, RenewalSummary, Options, Tags

## Handler Counts
- 16 total operations
- Core: RequestCertificate, ImportCertificate, DescribeCertificate, GetCertificate, ListCertificates, DeleteCertificate, ExportCertificate
- Lifecycle: RenewCertificate, RevokeCertificate, UpdateCertificateOptions
- Tags: AddTagsToCertificate, ListTagsForCertificate, RemoveTagsFromCertificate
- Account: GetAccountConfiguration, PutAccountConfiguration
- Validation: ResendValidationEmail
